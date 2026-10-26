# Stage 6: FastAPI and Streamlit

**Session 4.** A non-programmer can now get the prediction: an API serves it, and a one-page web app shows it. The layout is `backend/`, `frontend/` and `data/`.

## What changed from Stage 5

- [`backend/app/main.py`](backend/app/main.py): a FastAPI app with `GET /health` and `GET /limits`, which returns each device's predicted limit date.
- [`frontend/app.py`](frontend/app.py): a Streamlit page that calls the API and shows a table.
- Two new tests in [`backend/tests/test_api.py`](backend/tests/test_api.py). Tests and CI carry forward from Stage 5.

## How to run

Two terminals, both from this folder, with a Python 3.12 virtual environment.

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install -e './backend[dev]'
.venv/bin/python -m pip install -r frontend/requirements.txt
.venv/bin/python -m pytest backend       # expect 8 passed
```

Terminal 1, the API:

```bash
.venv/bin/python -m uvicorn app.main:app --app-dir backend --host 127.0.0.1 --port 8000
```

Terminal 2, the page:

```bash
.venv/bin/python -m streamlit run frontend/app.py --server.address 127.0.0.1 --server.port 8501
```

## What to expect

- `curl http://127.0.0.1:8000/limits` returns the limit (`100000`) and one date per device: `DEV-A` 2026-06-30, `DEV-B` 2026-04-01, `DEV-C` 2026-01-16.
- <http://127.0.0.1:8501> shows the same dates in a table.
- If the API terminal is not running, the page shows "Could not reach the API".

**The pain:** it works only on a correctly set-up machine, with two terminals open, the right Python and the right packages.

**Fixed by:** Docker and Compose (Session 4). **Next:** [Stage 7](../stage-7-docker/README.md).
