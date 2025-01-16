"""

Write a Python unit test program to check if a string is a palindrome.

The unit test should work OK on the following tests:

madam   =>  palindrome
hello   =>  non-palindrome

"""

import unittest


def is_palindrome(s: str) -> bool:
    return s == s[::-1]


class TestStrPalindrome(unittest.TestCase):
    """A unit test to test whether two strings are palindrome"""
    def test_on_palindrome_strings(self):
        """Test the logic on a palindrome string"""
        self.assertTrue(is_palindrome("madam"), f"The string is not palindrome")

    def test_on_non_palindrome_strings(self):
        """Test the logic on a non-palindrome string"""
        self.assertFalse(is_palindrome("hello"), f"The string is palindrome")


if __name__ == "__main__":
    unittest.main(verbosity=2)
