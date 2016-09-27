import unittest
from solution import Solution


test_data = range(1000)

sln = Solution(test_data)

class solution_test(unittest.TestCase):
    def test_no_repeats(self):
        k = 1000
        self.assertEqual(len(set(sln.solve(k))), k)

    def test_k_too_large(self):
        with self.assertRaises(ValueError):
            sln.solve(1001)

