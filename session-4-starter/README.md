# Session 4 starter files

Copy these into your Backend repo (the defaults `device_limit` and `model` are assumed; adjust the import in `api.py` if you chose other names):

| File | Copy to |
| --- | --- |
| `api.py` | `src/device_limit/api.py` |
| `Dockerfile` | repo root |
| `compose.yaml` | repo root |
| `.dockerignore` | repo root |

Then add an optional `api` extra under `[options.extras_require]` in `setup.cfg`, and `httpx` to the `test` extra so you can test the API:

```ini
api = fastapi; uvicorn; python-multipart
```

Install and run locally:

```bash
pip install -e '.[api,test]'
uvicorn device_limit.api:app --port 8000
curl -F file=@data/device_counts.csv http://127.0.0.1:8000/predict
```

Run both services:

```bash
docker compose up --build
```

Open <http://localhost:8501>, upload `data/device_counts.csv`, and check the table against `limits.csv`.

The frontend is built from the pinned tag `v1.0.0` of the Frontend repo. Do not edit it.
