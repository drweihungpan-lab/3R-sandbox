"""Load the device counts, one device at a time."""

import pandas as pd


def load_all(path="data/device_counts.csv"):
    raw = pd.read_csv(path, parse_dates=["date"])
    return pd.concat([part for _, part in raw.groupby("device_id")], ignore_index=True)
