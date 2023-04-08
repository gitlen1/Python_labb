
import unittest

from day01_part02 import calculate_fuel

class TestFuelCalculation(unittest.TestCase):
    def test_example(self):
        self.assertEqual(calculate_fuel([12]), 2)
        self.assertEqual(calculate_fuel([14]), 2)
        self.assertEqual(calculate_fuel([1969]), 654)
        self.assertEqual(calculate_fuel([100756]), 33583)

    def test_edges(self):
        self.assertEqual(calculate_fuel([0]), -2)
        self.assertEqual(calculate_fuel([1]), -2)
        self.assertEqual(calculate_fuel([2]), -2)

    def test_cases(self):
        self.assertEqual(calculate_fuel([12, 14, 1969, 100756]), 34241)


if __name__ == '__main__':
    unittest.main()
