# Stage 1: one notebook, copied as v1, v2, v3

**Session 1.** The whole analysis is one notebook. Each time the method changed, the notebook was copied and edited, so there are three copies.

## What is here

| File | What it does differently |
| --- | --- |
| `analysis_v1.ipynb` | Fits a line to every day. |
| `analysis_v2.ipynb` | Uses only the last 180 days. |
| `analysis_v3.ipynb` | Last 180 days, and leaves out zero-count days. |
| `data/device_counts.csv` | The synthetic data (see the [repository README](../README.md)). |

## How to run

Open a notebook in Jupyter or VS Code and run all cells. Run it from this folder so `data/device_counts.csv` is found. The notebooks need `pandas` and `numpy`.

## What to expect

Each notebook prints one limit date per device. The three copies print **different dates** (for example `DEV-C`: 2026-01-30, 2026-01-28, 2026-01-26).

```text
analysis_v1: DEV-A 2026-07-31, DEV-B 2026-04-21, DEV-C 2026-01-30
analysis_v2: DEV-A 2026-08-04, DEV-B 2026-04-21, DEV-C 2026-01-28
analysis_v3: DEV-A 2026-07-14, DEV-B 2026-04-10, DEV-C 2026-01-26
```

**The pain:** last month's report said a date, and nobody can say which copy produced it.

**Fixed by:** Git (Session 1). One history replaces `v1`/`v2`/`v3` copies.

**Next:** [Stage 2](../stage-2-python-files/README.md).
