"""

Write a Python unit test program to check if a function correctly parses and validates input data.
Note:   the data should be a numeric string which its corresponding int value greater zero.
        if the data is not of the type string or is not numeric, the parsing function should raise TypeError

The unit test should work OK on the following tests:

"100"                                       =>  valid data
"0", 1, 4.4, "hello", "45s", "-100"         =>  invalid data

"""

import unittest


def parse(d: str) -> bool:
    if isinstance(d, str) and d.isnumeric():
        return int(d) > 0
    else:
        raise ValueError


class TestDataValidity(unittest.TestCase):
    """A unit test to check the data validity"""
    def test_on_valid_data(self):
        """Test on valid data"""
        self.assertTrue(parse("100"), "The data is invalid")

    def test_on_invalid_data(self):
        """Test on invalid data"""
        with self.subTest("Testing on zero"):
            self.assertFalse(parse("0"), "The data is valid")

        data = [1, 4.4, "hello", "45s", "-100"]
        for sample in data:
            with self.subTest(f"Testing on {sample}"):
                with self.assertRaises(ValueError):
                    parse(sample)


if __name__ == "__main__":
    unittest.main(verbosity=2)
