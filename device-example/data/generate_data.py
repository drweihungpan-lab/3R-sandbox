"""Generate the synthetic daily measurement counts used by every stage.

Run from the repository root:

    python data/generate_data.py

The generator uses only the Python standard library and a fixed seed, so every
run writes byte-identical output to data/device_counts.csv.
"""

import csv
import random
from datetime import date, timedelta
from pathlib import Path

SEED = 20250101
START = date(2025, 1, 1)
DAYS = 365
# Typical measurements per day for each device (a roughly linear trend).
DEVICES = {"DEV-A": 180, "DEV-B": 220, "DEV-C": 260}
NOISE = 0.12  # standard deviation as a fraction of the typical count
ZERO_DAY_CHANCE = 0.03  # maintenance days with no measurements
OUTPUT = Path(__file__).resolve().parent / "device_counts.csv"


def generate_rows():
    rng = random.Random(SEED)
    for device_id, typical in DEVICES.items():
        for offset in range(DAYS):
            if rng.random() < ZERO_DAY_CHANCE:
                count = 0
            else:
                count = max(1, round(rng.gauss(typical, typical * NOISE)))
            yield device_id, (START + timedelta(days=offset)).isoformat(), count


def main():
    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["device_id", "date", "daily_count"])
        writer.writerows(generate_rows())
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
