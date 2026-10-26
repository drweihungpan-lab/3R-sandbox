"""Print the limit date for each device (the notebook does the same)."""

from loader import load_all
from model import limit_dates

for device, date in limit_dates(load_all()).items():
    print(device, "reaches the limit on", date)
