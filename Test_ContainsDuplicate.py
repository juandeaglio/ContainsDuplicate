import unittest
from main import Solution


class ContainsDuplicate(unittest.TestCase):
    def test_contains_duplicate_simple_case(self):
        self.assertEqual(True, Solution().containsDuplicate([1, 2, 3, 1]))


if __name__ == '__main__':
    unittest.main()
