"""Predict the date each device reaches its usage limit."""

import numpy as np
import pandas as pd

LIMIT = 100_000


def limit_dates(totals, limit=LIMIT):
    """`totals` holds each device's running total in the `daily_count` column."""
    dates = {}
    for device, g in totals.groupby("device_id"):
        g = g.sort_values("date")
        slope, intercept = np.polyfit(np.arange(len(g)), g["daily_count"].to_numpy(), 1)
        days = int(np.ceil((limit - intercept) / slope))
        dates[device] = (g["date"].iloc[0] + pd.Timedelta(days=days)).date()
    return dates
