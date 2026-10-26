"""Read the synthetic daily measurement counts."""

from pathlib import Path

import pandas as pd

# The data folder sits next to `backend/`, wherever the program is run from.
DEFAULT_PATH = Path(__file__).resolve().parents[2] / "data" / "device_counts.csv"


def load_counts(path=DEFAULT_PATH):
    counts = pd.read_csv(path, parse_dates=["date"])
    # Tidy up: days without measurements are not useful.
    return counts[counts["daily_count"] > 0]
