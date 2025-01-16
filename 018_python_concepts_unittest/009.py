"""
Write a Python unit test program to check if a database query returns the expected results.

"018_python_concepts_unittest/008.db" is a database that have only one table 'exercises' with the following columns:
    ['date', 'exercise', 'author', 'framework']

Fetch all the contents of the 'exercises' table, and they should match the following:
    [('2025-01-16', 8, 'Mustafa Younes', 'unittest')]

"""

import pathlib
import unittest


class TestDatabaseTableContents(unittest.TestCase):
    """A unit test to test the contents in a database table"""
    __con = None
    __db_path = pathlib.Path("008.db")

    @classmethod
    def setUpClass(cls):
        """Test case setup routine"""
        import sqlite3

        assert pathlib.Path(cls.__db_path).is_file(), f"{cls.__db_path} doesn't exist"
        cls.__con = sqlite3.connect(cls.__db_path)
        cls.__cur = cls.__con.cursor()

    @classmethod
    def tearDownClass(cls):
        """Test case teardown routine"""
        cls.__con = cls.__con.close()

    def test_exercises_table_contents(self):
        """Test the contents of the 'exercises' table in the '008.db' database"""
        self.assertListEqual(
            self.__cur.execute("SELECT * FROM exercises").fetchall(),
            [('2025-01-16', 8, 'Mustafa Younes', 'unittest')],
            "Unexpected contents in the 'exercise' table in '008.db'"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
