# Stage 7: Docker

**Session 4.** Docker Compose starts the API and the page together, and the limit dates from a local run and a Docker run are identical.

## What changed from Stage 6

- [`backend.Dockerfile`](backend.Dockerfile) and [`frontend.Dockerfile`](frontend.Dockerfile) build the two services from `python:3.12-slim`.
- [`compose.yaml`](compose.yaml) starts both. The page reaches the API at `http://backend:8000`, the service name.
- `load_counts()` accepts a `DEVICE_DATA_PATH` environment variable, because the container installs the package outside the repository.
- [`compare_limit_dates.py`](compare_limit_dates.py) compares the `/limits` output of two running services, exactly.
- Tests and CI carry forward from Stage 5.

## How to run

You need a running Docker engine with Compose v2.

```bash
cd stage-7-docker
docker compose up --build -d --wait
```

The API is at <http://127.0.0.1:8000/limits> and the page at <http://127.0.0.1:8501>.

To compare with a local run, start the Stage 6 API on another port (see [Stage 6](../stage-6-api-ui/README.md)) and compare the two:

```bash
# in another terminal, from the stage-6-api-ui folder, with its .venv
.venv/bin/python -m uvicorn app.main:app --app-dir backend --port 8001

# from the stage-7-docker folder
python3 compare_limit_dates.py http://127.0.0.1:8001 http://127.0.0.1:8000
```

Stop the containers with `docker compose down`.

## What to expect

```text
local  DEV-A 2026-06-30
local  DEV-B 2026-04-01
local  DEV-C 2026-01-16
docker DEV-A 2026-06-30
docker DEV-B 2026-04-01
docker DEV-C 2026-01-16
MATCH: local and Docker limit dates are identical
```

Under the course definitions, the same code and data in a slightly different environment give the same dates: replicability.

**The pain removed:** no more "works on my machine". The last stage of the story. In Session 5, tell the whole story from Stage 1 to here.
