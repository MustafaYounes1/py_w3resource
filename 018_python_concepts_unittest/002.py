"""

Write a Python unit test program to check if a list is sorted in ascending order.

The unit test should work OK on the following tests:

[1, 2, 3, 4, 5, 6, 7]   =>  sorted
[5, 7, 2, 8, 1, 9]      =>  not sorted

"""

import unittest


def is_sorted_ascending(lst: list) -> bool:
    return all(a <= b for a, b in zip(lst[:-1], lst[1:]))


class TestSortedList(unittest.TestCase):
    """A unit test to test the logic of determining whether a list is sorted or not"""
    def test_on_sorted_list(self):
        """Test the logic on a sorted list"""
        self.assertTrue(is_sorted_ascending([1, 2, 3, 4, 5, 6, 7]), "The list is not sorted in an ascending order!")

    def test_on_non_sorted_list(self):
        """Test the logic on a non-sorted list"""
        self.assertFalse(is_sorted_ascending([5, 7, 2, 8, 1, 9]), "The list is sorted in an ascending order!")


if __name__ == "__main__":
    unittest.main(verbosity=2)
