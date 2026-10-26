from datetime import date

import pandas as pd
import pytest

from device_limit import LIMIT, load_counts, predict_limit_dates
from device_limit.model import add_late_arrivals, running_totals

EXPECTED_LIMIT_DATES = {
    "DEV-A": date(2026, 6, 30),
    "DEV-B": date(2026, 4, 1),
    "DEV-C": date(2026, 1, 16),
}


def test_limit_dates_are_pinned_for_the_fixed_synthetic_data():
    assert predict_limit_dates(load_counts()) == EXPECTED_LIMIT_DATES


def test_loads_all_devices_and_days():
    counts = load_counts()
    assert counts["device_id"].nunique() == 3
    assert len(counts) == 3 * 365


def test_loading_does_not_depend_on_the_working_folder(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    assert len(load_counts()) == 3 * 365


def test_running_totals_end_at_the_sum_of_daily_counts():
    counts = load_counts()
    totals = running_totals(counts)
    last = totals.groupby("device_id")["total"].last()
    assert last.to_dict() == counts.groupby("device_id")["daily_count"].sum().to_dict()


def test_adding_late_arrivals_does_not_change_its_input():
    totals = running_totals(load_counts())
    before = totals["total"].copy()
    add_late_arrivals(totals)
    pd.testing.assert_series_equal(totals["total"], before)


def test_a_device_that_never_gets_close_still_gets_a_date_after_its_data():
    counts = pd.DataFrame(
        {
            "device_id": ["X"] * 10,
            "date": pd.date_range("2025-01-01", periods=10),
            "daily_count": [10] * 10,
        }
    )
    assert predict_limit_dates(counts, limit=LIMIT)["X"] > date(2025, 1, 10)
