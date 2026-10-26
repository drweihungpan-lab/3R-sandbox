"""FastAPI service that returns each device's predicted limit date."""

from fastapi import FastAPI, File, HTTPException, UploadFile

from device_limit.model import load_counts, predict_limit_dates

app = FastAPI(title="Device limit API")


@app.get("/health")
def health():
    """Report that the service is ready."""
    return {"status": "ok"}


@app.post("/predict")
def predict(file: UploadFile = File(...)):
    """Return the limit date of each device in the uploaded CSV."""
    try:
        dates = predict_limit_dates(load_counts(file.file, label=file.filename))
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error)) from error
    return {
        "devices": [
            {"device_id": device_id, "limit_date": limit_date.isoformat()}
            for device_id, limit_date in sorted(dates.items())
        ]
    }
