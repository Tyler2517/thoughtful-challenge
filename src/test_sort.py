import unittest
from sort import sort

class TestPackageSort(unittest.TestCase):
    def test_standard_packages(self):
        self.assertEqual(sort(10, 10, 10, 1), "STANDARD")
        self.assertEqual(sort(50, 50, 50, 10), "STANDARD")

    def test_special_packages(self):
        self.assertEqual(sort(200, 100, 50, 15), "SPECIAL")
        self.assertEqual(sort(50, 50, 50, 25), "SPECIAL")
        self.assertEqual(sort(300, 300, 200, 10), "SPECIAL")

    def test_rejected_packages(self):
        self.assertEqual(sort(200, 200, 200, 25), "REJECTED")
        self.assertEqual(sort(150, 150, 150, 20), "REJECTED")

    def test_edge_cases(self):
        self.assertEqual(sort(100, 100, 100, 20), "REJECTED")
        self.assertEqual(sort(150, 10, 10, 19.9), "SPECIAL")
        self.assertEqual(sort(10, 10, 10, 0.1), "STANDARD") 

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            sort("a", 100, 100, 10)
        with self.assertRaises(ValueError):
            sort(100, -10, 100, 10)
        with self.assertRaises(ValueError):
            sort(0, 100, 100, 10)

    def test_valid_decimals(self):
        self.assertEqual(sort(100.5, 100.5, 100.5, 10.5), "SPECIAL")
        self.assertEqual(sort(150.1, 100, 100, 10), "SPECIAL")
        self.assertEqual(sort(150, 150, 150, 20.5), "REJECTED")

if __name__ == "__main__":
    unittest.main()
