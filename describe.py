#!/usr/bin/env python3
"""Quick column summary for a CSV — made for stats homework and small datasets."""

from __future__ import annotations

import argparse
import csv
import math
import sys
from collections import Counter
from pathlib import Path
from typing import Iterable


def is_number(value: str) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False


def mean(nums: list[float]) -> float:
    return sum(nums) / len(nums)


def median(nums: list[float]) -> float:
    ordered = sorted(nums)
    n = len(ordered)
    mid = n // 2
    if n % 2:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2


def sample_sd(nums: list[float]) -> float | None:
    if len(nums) < 2:
        return None
    m = mean(nums)
    var = sum((x - m) ** 2 for x in nums) / (len(nums) - 1)
    return math.sqrt(var)


def mode_labels(values: Iterable[str]) -> str:
    counts = Counter(v for v in values if v != "")
    if not counts:
        return "—"
    top = max(counts.values())
    modes = sorted(k for k, c in counts.items() if c == top)
    return ", ".join(modes[:3]) + ("…" if len(modes) > 3 else "")


def describe_column(name: str, cells: list[str]) -> None:
    nonempty = [c.strip() for c in cells if c.strip() != ""]
    missing = len(cells) - len(nonempty)
    numeric = [float(c) for c in nonempty if is_number(c)]
    numeric_share = (len(numeric) / len(nonempty)) if nonempty else 0.0

    print(f"\n## {name}")
    print(f"rows: {len(cells)}  |  non-empty: {len(nonempty)}  |  missing: {missing}")

    if nonempty and numeric_share >= 0.8 and numeric:
        sd = sample_sd(numeric)
        sd_txt = f"{sd:.4g}" if sd is not None else "—"
        print(
            "type: numeric\n"
            f"min: {min(numeric):.4g}  max: {max(numeric):.4g}\n"
            f"mean: {mean(numeric):.4g}  median: {median(numeric):.4g}  sd: {sd_txt}"
        )
    else:
        uniq = len(set(nonempty))
        print(f"type: categorical  |  unique: {uniq}")
        print(f"mode: {mode_labels(nonempty)}")


def read_csv(path: Path) -> tuple[list[str], list[list[str]]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        try:
            header = next(reader)
        except StopIteration:
            raise SystemExit(f"empty file: {path}")
        rows = [row for row in reader]
    return header, rows


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Print a short summary of each CSV column (mean/median/sd or modes)."
    )
    parser.add_argument("csv", type=Path, help="path to a .csv file")
    parser.add_argument(
        "--max-cols",
        type=int,
        default=20,
        help="stop after this many columns (default: 20)",
    )
    args = parser.parse_args()

    if not args.csv.is_file():
        raise SystemExit(f"file not found: {args.csv}")

    header, rows = read_csv(args.csv)
    width = max(len(h) for h in header) if header else 0
    print(f"{args.csv.name} — {len(rows)} data rows, {len(header)} columns")

    for i, name in enumerate(header[: args.max_cols]):
        col = [(row[i] if i < len(row) else "") for row in rows]
        describe_column(name or f"col_{i+1}", col)

    if len(header) > args.max_cols:
        print(f"\n… {len(header) - args.max_cols} more columns not shown (raise --max-cols)")


if __name__ == "__main__":
    main()
