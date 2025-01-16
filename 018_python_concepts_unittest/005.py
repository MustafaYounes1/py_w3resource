"""

Write a Python unit test program to check if a file exists in a specified directory.

The unit test should work OK on the following tests:

The current module exists   =>  True

"""

import pathlib
import unittest


class TestFileExistence(unittest.TestCase):
    """A unit test to test whether a file exists"""

    def test_on_existed_file(self):
        """Test whether the current executing module exists (A silly test)"""
        self.assertTrue(pathlib.Path(__file__).is_file(), f"{pathlib.Path(__file__).absolute()} does not exist")


if __name__ == "__main__":
    unittest.main(verbosity=2)
