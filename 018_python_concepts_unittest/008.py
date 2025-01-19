"""

Write a Python unit test program to check if a database connection is successful.

"018_python_concepts_unittest/008.db" is a database that have only one table 'exercises' with the following columns:
    ['date', 'exercise', 'author', 'framework']
    
Create a unit test that creates a connection to that database and checks whether it has the expected tables and columns

"""

from operator import itemgetter
import pathlib
import unittest


_db_path = pathlib.Path("008.db")


@unittest.skipUnless(_db_path.is_file(), f"The database file: {_db_path} is missing")
class TestDatabaseConnection(unittest.TestCase):
    """A unit test to test the successful connection to a database"""
    __con = None

    @classmethod
    def setUpClass(cls):
        """Test case setup routine"""
        import sqlite3

        cls.__con = sqlite3.connect(_db_path)
        cls.__cur = cls.__con.cursor()

    @classmethod
    def tearDownClass(cls):
        """Test case teardown routine"""
        cls.__con = cls.__con.close()

    def test_connection_to_database(self):
        """Test the successful connection to '008.db'"""
        self.assertListEqual(
            self.__cur.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall(),
            [("exercises",)],
            "Unexpected tables names"
        )

        column_names = list(map(itemgetter(1), self.__cur.execute("PRAGMA table_info(exercises);").fetchall()))

        self.assertListEqual(
            column_names,
            ['date', 'exercise', 'author', 'framework'],
            "Unexpected column names"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
