"""Read the synthetic daily measurement counts."""

import pandas as pd


def load_counts(path="data/device_counts.csv"):
    return pd.read_csv(path, parse_dates=["date"])
