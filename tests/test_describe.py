import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import describe  # noqa: E402


class StatsTests(unittest.TestCase):
    def test_median_odd_and_even(self):
        self.assertEqual(describe.median([3, 1, 2]), 2)
        self.assertEqual(describe.median([4, 1, 3, 2]), 2.5)

    def test_sample_sd(self):
        self.assertIsNone(describe.sample_sd([5.0]))
        self.assertAlmostEqual(describe.sample_sd([88, 72, 91, 72, 85]), 9.017, places=3)

    def test_is_number(self):
        self.assertTrue(describe.is_number("3.5"))
        self.assertTrue(describe.is_number("-2"))
        self.assertFalse(describe.is_number("Dhaka"))

    def test_mode_labels(self):
        self.assertEqual(describe.mode_labels(["a", "b", "a"]), "a")
        self.assertEqual(describe.mode_labels(["x", "y"]), "x, y")
        self.assertEqual(describe.mode_labels(["", ""]), "—")


class CliTests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, str(ROOT / "describe.py"), *args],
            capture_output=True,
            text=True,
        )

    def test_sample_csv(self):
        result = self.run_cli(str(ROOT / "sample.csv"))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("5 data rows, 3 columns", result.stdout)
        self.assertIn("mean: 81.6  median: 85  sd: 9.017", result.stdout)

    def test_missing_file(self):
        result = self.run_cli("does-not-exist.csv")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("file not found", result.stderr)

    def test_max_cols(self):
        result = self.run_cli(str(ROOT / "sample.csv"), "--max-cols", "1")
        self.assertIn("2 more columns not shown", result.stdout)


if __name__ == "__main__":
    unittest.main()
