# csv-describe

Stdlib-only Python CLI: mean, median, and sample standard deviation for numeric columns; unique count and mode for categorical ones.

## Problem

A one-command glance at a small CSV before opening a stats notebook, without pandas.

## How to run

Python 3. Nothing to install.

```bash
python3 describe.py sample.csv
python3 describe.py data.csv --max-cols 10
```

`--max-cols` stops after that many columns (default 20).

## Example

```text
sample.csv — 5 data rows, 3 columns

## name
rows: 5  |  non-empty: 5  |  missing: 0
type: categorical  |  unique: 5
mode: Ada, Ben, Cara…

## score
rows: 5  |  non-empty: 5  |  missing: 0
type: numeric
min: 72  max: 91
mean: 81.6  median: 85  sd: 9.017

## city
rows: 5  |  non-empty: 5  |  missing: 0
type: categorical  |  unique: 3
mode: Cumilla, Dhaka
```

## License

MIT
