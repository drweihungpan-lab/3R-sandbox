# 3R-device-example

A running example for the course *Repeatability, Reproducibility, and Replicability*: **one statistical analysis growing up in seven stages**, from a messy notebook to a tested, containerized application.

The instructor tells the story of the stages in each session. The same device data is the dataset for the course's hands-on work: in Session 2 each group's package is generated from the course cookiecutter and contains the Stage 4 processing code. The stage folders here show *why* each tool exists; your own repository is where you practise *how*.

## The scenario

Daily measurement counts for three medical devices (`DEV-A`, `DEV-B`, `DEV-C`) over about one year. Each device has a fixed **usage limit** of **100,000 measurements** in total. The task is to predict the date each device reaches its limit. The model is a straight line fitted to each device's running total, extended until it reaches the limit. It is deliberately simple; the point is the engineering around it.

## The seven stages

Each stage is a complete, runnable snapshot in its own folder with a README saying what changed, how to run it, the symptom to expect, and which session's tool fixes it.

| Stage | Folder | What's added | Visible symptom | Session |
| --- | --- | --- | --- | --- |
| 1 | [stage-1-notebook-copies](stage-1-notebook-copies/) | One notebook, copied as `v1`/`v2`/`v3` | Nobody can say which copy produced the reported limit date | 1 |
| 2 | [stage-2-python-files](stage-2-python-files/) | `.py` files imported by the notebook, no declared dependencies | Works with pandas 1.5, crashes with pandas 2.x | 1 |
| 3 | [stage-3-requirements](stage-3-requirements/) | `requirements.txt`, not a package | Rerunning a cell moves the limit date weeks earlier, with no error | 2 |
| 4 | [stage-4-package](stage-4-package/) | Installable package, no tests, no UI | Fails from another folder; a "cleanup" silently moves the date | 2 |
| 5 | [stage-5-tests-ci](stage-5-tests-ci/) | Tests and CI | CI turns red on that same cleanup; only programmers can get a prediction | 3 |
| 6 | [stage-6-api-ui](stage-6-api-ui/) | FastAPI and Streamlit | Works only on a correctly set-up machine, with two terminals | 4 |
| 7 | [stage-7-docker](stage-7-docker/) | Docker | Local and Docker give the same limit date | 4 |

Stages 5–7 use a processing package, an API, a page, tests and Compose under the package name `device_limit`.

## Data and provenance

[`data/device_counts.csv`](data/device_counts.csv) is **synthetic**. It does not come from real devices or real patients. It is produced by [`data/generate_data.py`](data/generate_data.py), which uses a fixed seed (`20250101`) and only the Python standard library:

- 3 devices × 365 days (2025-01-01 to 2025-12-31), columns `device_id`, `date`, `daily_count`.
- A typical count per day of 180, 220 and 260 (a roughly linear trend), with random noise of about 12%.
- About 3% of days are maintenance days with a count of 0.

Running the generator twice writes byte-identical data (SHA-256 `92031a201aaae60d9802fba68afc1f8aa59e997c612bbaef9fd1d328d0b33e5d`). Each stage folder holds its own copy of the data so the folders stay complete snapshots.

```bash
python3 data/generate_data.py
```

## Checks

Stages 5–7 pass their own tests, run by [CI](../.github/workflows/device-example.yml) on every push and pull request. The branch `demo/cleanup-drops-zero-days` is the Session 3 demonstration: its pull request shows CI failing. It is never merged.
