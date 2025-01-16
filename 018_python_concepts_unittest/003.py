"""

Write a Python unit test program that checks if two lists are equal.

The unit test should work OK on the following tests:

[10, 20, 30, 40], [10, 20, 30, 40]      => Equal
[10, 20, 30, 40], [30, 20, 10, 40]      => Not-equal

"""

import unittest


class TestListEquality(unittest.TestCase):
    """A unit test to test lists equality"""
    def test_on_equal_lists(self):
        """Check equal lists"""
        self.assertListEqual([10, 20, 30, 40], [10, 20, 30, 40], "The two lists are not equal")

    def assertListNotEqual(self, lst1: list, lst2: list):
        """A custom assertion to assert that two lists are not equal"""
        self.assertFalse(lst1 == lst2, "The two lists are equal")

    def test_on_not_equal_lists(self):
        """Check on not-equal lists"""
        self.assertListNotEqual([10, 20, 30, 40], [30, 20, 10, 40])


if __name__ == "__main__":
    unittest.main(verbosity=2)
