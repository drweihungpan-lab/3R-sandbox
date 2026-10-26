"""FastAPI service that returns each device's predicted limit date."""

from fastapi import FastAPI

from device_limit import LIMIT, load_counts, predict_limit_dates

app = FastAPI(title="Device limit API")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/limits")
def limits():
    dates = predict_limit_dates(load_counts())
    return {
        "limit": LIMIT,
        "devices": [
            {"device_id": device_id, "limit_date": date.isoformat()}
            for device_id, date in dates.items()
        ],
    }
