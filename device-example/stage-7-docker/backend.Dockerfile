FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEVICE_DATA_PATH=/app/data/device_counts.csv

WORKDIR /app

# Build from this stage's folder; install only the declared runtime dependencies.
COPY backend/pyproject.toml ./
COPY backend/app/ ./app/
COPY backend/device_limit/ ./device_limit/
RUN python -m pip install --no-cache-dir .

COPY data/device_counts.csv ./data/device_counts.csv

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
