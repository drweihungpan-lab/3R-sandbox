"""Read the synthetic daily measurement counts."""

import os
from pathlib import Path

import pandas as pd

# By default the data folder sits next to `backend/`. A container installs the
# package elsewhere, so DEVICE_DATA_PATH can point to the file instead.
DEFAULT_PATH = Path(__file__).resolve().parents[2] / "data" / "device_counts.csv"


def load_counts(path=None):
    path = path or os.environ.get("DEVICE_DATA_PATH") or DEFAULT_PATH
    return pd.read_csv(path, parse_dates=["date"])
