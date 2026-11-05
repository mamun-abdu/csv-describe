# csv-describe

Tiny Python CLI that prints a quick summary of each CSV column — mean / median / sd for numeric fields, unique counts and mode for categorical ones.

Built for stats homework and small datasets. Stdlib only (no pandas).

## Usage

```bash
python3 describe.py sample.csv
python3 describe.py data.csv --max-cols 10
```

## Example

```text
sample.csv — 5 data rows, 3 columns

## score
type: numeric
min: 72  max: 91
mean: 81.6  median: 85  sd: 9.017
```

## Why

I kept reaching for a one-file way to glance at a CSV before opening a notebook. This is that glance.

## License

MIT
