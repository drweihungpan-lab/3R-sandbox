# Stage 2: helper `.py` files, no declared dependencies

**Session 1.** The notebook now imports `loader.py` and `model.py`, so the code can be reused. Nothing records which packages, or which versions, it needs.

## What changed from Stage 1

- Loading and the model moved out of the notebook into [`loader.py`](loader.py) and [`model.py`](model.py).
- [`report.py`](report.py) prints the same dates as the notebook, which is easier to run from a terminal.
- `loader.py` uses `DataFrame.append`, which was **removed in pandas 2.0**.

## How to run

Create two environments (the instructor steps are in the Session 1 notes of the course repository).

```bash
# "My laptop": Python 3.11 with pandas 1.5
python3.11 -m venv .venv311
.venv311/bin/python -m pip install "pandas==1.5.3" "numpy<2"
.venv311/bin/python report.py

# "Colleague's laptop": Python 3.12 with pandas 2.x
python3.12 -m venv .venv312
.venv312/bin/python -m pip install "pandas>=2.2,<3"
.venv312/bin/python report.py
```

pandas 1.5 does not support Python 3.12, which is why "my laptop" is Python 3.11. Run from this folder so `data/device_counts.csv` is found.

## What to expect

- **Python 3.11 + pandas 1.5:** prints a deprecation warning, then the dates:

  ```text
  DEV-A reaches the limit on 2026-07-31
  DEV-B reaches the limit on 2026-04-21
  DEV-C reaches the limit on 2026-01-30
  ```

- **Python 3.12 + pandas 2.x:** crashes with `AttributeError: 'DataFrame' object has no attribute 'append'`.

**The pain:** the same files work on one machine and crash on another, and nothing says why.

**Fixed by:** declaring dependencies with `requirements.txt` (Session 2) so the other machine installs what the code needs.

**Next:** [Stage 3](../stage-3-requirements/README.md).
