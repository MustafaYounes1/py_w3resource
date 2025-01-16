"""

Write a Python unit test program to check if a given number is prime or not.

The unit test should work OK on the following tests:

Prime numbers:      2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31
Non-prime numbers:  4, 6, 8, 10, 12, 14, 16, 18, 20

"""

from math import sqrt
import unittest


def is_prime(n: int) -> bool:
    if n <= 1:
        return False

    for _ in range(2, int(sqrt(n)) + 1):
        if n % 2 == 0:
            return False

    return True


class TestPrimeNumbers(unittest.TestCase):
    """A unit test for testing the logic of determining whether a number is prime or not"""
    def test_on_prime_numbers(self):
        """Test the logic on a prime numbers"""
        for number in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
            with self.subTest(f"Testing on: {number}", number=number):
                self.assertTrue(is_prime(number))

    def test_on_non_prime_numbers(self):
        """Test the logic on a non-prime numbers"""
        for number in [4, 6, 8, 10, 12, 14, 16, 18, 20]:
            with self.subTest(f"Testing on: {number}", number=number):
                self.assertFalse(is_prime(number))


if __name__ == "__main__":
    unittest.main(verbosity=2)
