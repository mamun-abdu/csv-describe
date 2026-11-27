# csv-describe

A one-file Python CLI that gives you a quick summary of every column in a CSV. Numeric columns get min, max, mean, median, and standard deviation. Text columns get a unique count and the most common value(s).

It uses only the Python standard library, so there is no pandas and nothing to install. I use it for a first look at small datasets before opening a notebook.

## Run it

You need Python 3.10 or newer.

```bash
git clone https://github.com/mamun-abdu/csv-describe.git
cd csv-describe
python3 describe.py sample.csv
```

Options:

- `--max-cols N` stops after the first `N` columns (default 20).

```bash
python3 describe.py data.csv --max-cols 10
```

## Example

Running it on the included `sample.csv`:

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

## How it decides

- A column counts as **numeric** when at least 80% of its non-empty cells parse as numbers. Cells that don't parse are left out of the numeric stats.
- **sd** is the sample standard deviation (divides by n − 1). It shows `—` when there are fewer than two numbers.
- **mode** lists up to three tied values, sorted, with `…` when there are more. When every value is different, every value is a tie, so the first three are shown.
- Empty cells count as missing. A UTF-8 byte-order mark (common in files saved from Excel) is handled.

## Tests

```bash
python3 -m unittest discover -s tests -v
```

## License

MIT. See [LICENSE](LICENSE).
