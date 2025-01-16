"""

Write a Python unit test that checks if a function handles floating-point calculations accurately.

The unit test should work OK on the following tests:

0.3 + 0.5   ==  0.81        (with 1 decimal place)
0.3 * 0.5   ==  0.152       (with 2 decimal places)
0.7 / 0.3   ==  2.333333    (with 6 decimal places)

"""

import unittest


class TestFloatOperationPrecision(unittest.TestCase):
    """A test unit to test the accuracy of some float calculations"""
    def test_summation(self):
        """Test the accuracy on the summation operation"""
        self.assertAlmostEqual(0.3 + 0.5, 0.81, places=1, msg="The operation is not accurate")

    def test_multiplication(self):
        """Test the accuracy on the multiplication operation"""
        self.assertAlmostEqual(0.3 * 0.5, 0.152, places=2, msg="The operation is not accurate")

    def test_division(self):
        """Test the accuracy on the division operation"""
        self.assertAlmostEqual(0.7 / 0.3, 2.333333, places=6, msg="The operation is not accurate")


if __name__ == "__main__":
    unittest.main(verbosity=2)
