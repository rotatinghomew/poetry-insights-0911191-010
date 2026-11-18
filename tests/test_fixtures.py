import csv
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class FixtureTests(unittest.TestCase):
    def test_csv_rows_have_consistent_columns(self):
        for path in (ROOT / "data").glob("*.csv"):
            with path.open(encoding="utf-8", newline="") as source:
                rows = list(csv.reader(source))
            self.assertGreaterEqual(len(rows), 2, path.name)
            self.assertTrue(rows[0], path.name)
            self.assertTrue(all(len(row) == len(rows[0]) for row in rows), path.name)

if __name__ == "__main__":
    unittest.main()
