# Stage 3: `requirements.txt`, still a notebook plus scripts

**Session 2.** Stage 2's crash is fixed by declaring the dependencies. The analysis is still a notebook that imports helper files.

## What changed from Stage 2

- [`requirements.txt`](requirements.txt) declares `pandas>=2.2,<3` and `numpy`, so another machine installs what the code needs.
- [`loader.py`](loader.py) uses `pd.concat` instead of the removed `DataFrame.append`.
- The notebook [`analysis.ipynb`](analysis.ipynb) now turns daily counts into running totals **in place**, and a later cell adds 10,000 late-arriving measurements to the totals in place.

## How to run

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pip install notebook   # or open the notebook in VS Code
```

Open `analysis.ipynb` from this folder and **Run All**. Then run the cell that adds the late arrivals, and the last cell, once more.

## What to expect

- **Cells run once, in order:**

  ```text
  DEV-A reaches the limit on 2026-06-30
  DEV-B reaches the limit on 2026-04-01
  DEV-C reaches the limit on 2026-01-16
  ```

- **After rerunning the late-arrivals cell and the last cell**, with no error or warning, the dates move weeks earlier:

  ```text
  DEV-A reaches the limit on 2026-06-02
  DEV-B reaches the limit on 2026-03-14
  DEV-C reaches the limit on 2026-01-04
  ```

  Running cells out of order has the same effect: the notebook's state depends on what you ran before.

**The pain:** the notebook holds hidden state, so the same cells give a different answer the second time.

**Fixed by:** moving the analysis into a package of functions with inputs and outputs (Session 2).

**Next:** [Stage 4](../stage-4-package/README.md).
