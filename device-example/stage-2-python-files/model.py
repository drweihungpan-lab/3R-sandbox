"""Predict the date each device reaches its usage limit."""

import numpy as np
import pandas as pd

LIMIT = 100_000


def limit_dates(frame, limit=LIMIT):
    dates = {}
    for device, g in frame.groupby("device_id"):
        g = g.sort_values("date")
        total = g["daily_count"].cumsum().to_numpy()
        slope, intercept = np.polyfit(np.arange(len(g)), total, 1)
        days = int(np.ceil((limit - intercept) / slope))
        dates[device] = (g["date"].iloc[0] + pd.Timedelta(days=days)).date()
    return dates
