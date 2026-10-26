# Stage 4: an installable package, no tests, no UI

**Session 2.** The analysis is now a Python package, `device_limit`, with functions that take inputs and return results. It still has two weaknesses: a relative data path, and no tests.

## What changed from Stage 3

- [`device_limit/`](device_limit/) is a package with [`pyproject.toml`](pyproject.toml). `predict_limit_dates(counts)` takes a table and returns `{device_id: date}`.
- The in-place late-arrivals step became `add_late_arrivals(totals)`, which returns a new table instead of changing its input, so running it twice cannot double-count.
- `load_counts` reads `data/device_counts.csv` **relative to the folder you run from**.

## How to run

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install -e .
.venv/bin/python -m device_limit
```

Run from this folder.

## What to expect

From this folder, the same dates as Stage 3:

```text
DEV-A reaches the limit on 2026-06-30
DEV-B reaches the limit on 2026-04-01
DEV-C reaches the limit on 2026-01-16
```

**Symptom 1, another folder.** Run from anywhere else, for example `cd .. && stage-4-package/.venv/bin/python -m device_limit`:

```text
FileNotFoundError: [Errno 2] No such file or directory: 'data/device_counts.csv'
```

**Symptom 2, a "cleanup" that quietly moves the date.** [`cleanup-drop-zero-days.patch`](cleanup-drop-zero-days.patch) drops days with zero measurements, which looks harmless. From the repository root:

```bash
git apply device-example/stage-4-package/cleanup-drop-zero-days.patch
cd device-example/stage-4-package && .venv/bin/python -m device_limit
```

```text
DEV-A reaches the limit on 2026-06-10
DEV-B reaches the limit on 2026-03-16
DEV-C reaches the limit on 2026-01-06
```

There is no error and no warning, yet every date moved by weeks. The model counts rows as days, so removing rows shortens the timeline. Undo with `git checkout stage-4-package/device_limit/data.py`.

**The pain:** the package works only from one folder, and nothing notices a change that moves the answer.

**Fixed by:** tests and CI (Session 3). **Next:** [Stage 5](../stage-5-tests-ci/README.md).
