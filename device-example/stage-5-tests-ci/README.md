# Stage 5: tests and CI

**Session 3.** Stage 4's package gains tests, and CI runs them on every push and pull request.

## What changed from Stage 4

- [`backend/tests/`](backend/tests/) has six tests. One pins the expected limit date for each device on the fixed synthetic data.
- [`.github/workflows/ci.yml`](../.github/workflows/ci.yml) runs the tests for Stages 5, 6 and 7 on every push and pull request.
- The data path no longer depends on the working folder: `load_counts()` finds `data/device_counts.csv` next to `backend/`, so Stage 5 runs from any folder.
- The layout is `backend/`, `data/` and `tests/`.

## How to run

```bash
cd stage-5-tests-ci/backend
python3.12 -m venv .venv
.venv/bin/python -m pip install -e '.[dev]'
.venv/bin/python -m pytest
```

Expect `6 passed`. Run `.venv/bin/python -m device_limit` from any folder: the dates match Stage 4 (2026-06-30, 2026-04-01, 2026-01-16).

## Where to see CI

Open the repository's **Actions** tab. The `main` branch is green. The demo branch `demo/cleanup-drops-zero-days` applies the same "cleanup" as Stage 4 ([`cleanup-drop-zero-days.patch`](cleanup-drop-zero-days.patch)); its pull request shows CI **red** on exactly the bug that slipped through in Stage 4:

```text
FAILED tests/test_model.py::test_limit_dates_are_pinned_for_the_fixed_synthetic_data
3 failed, 3 passed
```

Locally, `git apply stage-5-tests-ci/cleanup-drop-zero-days.patch` from the repository root produces the same failures. Undo with `git checkout stage-5-tests-ci/backend/device_limit/data.py`.

**The pain:** the checks protect `main`, but only a programmer can get a prediction.

**Fixed by:** an API and a web page (Session 3, Session 4). **Next:** [Stage 6](../stage-6-api-ui/README.md).
