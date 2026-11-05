# QuantEcon Workspace

This repository is a clean workspace for working through self-guided QuantEcon lectures.

## Project layout

```text
quantecon/
├── data/
│   ├── external/      # third-party/source datasets
│   ├── processed/     # transformed data used in analysis
│   └── raw/           # immutable raw snapshots
├── notebooks/         # lecture and experiment notebooks
├── scripts/           # one-off or reusable data/maintenance scripts
├── src/
│   └── qe_custom/     # local package for shared helpers
└── tests/             # tests for local package code
```

## Quick start

1. Create and activate a Python environment.
2. Install in editable mode:

   ```bash
   python -m pip install -e ".[dev]"
   ```

3. Start JupyterLab:

   ```bash
   jupyter lab
   ```

## Notes

- Put reusable code in `src/qe_custom/` instead of duplicating notebook cells.
- Keep `data/raw/` immutable so you can reproduce transformations into `data/processed/`.
- Keep large datasets out of git unless explicitly needed.
