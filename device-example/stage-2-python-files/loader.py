"""Load the device counts, one device at a time."""

import pandas as pd


def load_all(path="data/device_counts.csv"):
    raw = pd.read_csv(path, parse_dates=["date"])
    frames = pd.DataFrame()
    for _, part in raw.groupby("device_id"):
        frames = frames.append(part, ignore_index=True)
    return frames
