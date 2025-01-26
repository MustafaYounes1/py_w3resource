"""

Write a Python program that implements a decorator to retry a function multiple times in case of failure.
    Try to open '006.db' and fetch all contents from the table 'STUDENT'
    retry 3 times with a delay of 2 seconds

"""

import sqlite3
import time
from typing import Callable


def try_to_query_db(n_trials: int, delay: int) -> Callable[..., ...]:
    def outer(func: Callable[..., ...]) -> Callable[..., ...]:
        def inner(*args, **kwargs) -> ...:
            for _ in range(n_trials):
                try:
                    res = func(*args, **kwargs)
                    return res
                except sqlite3.Error as e:
                    print(f"Error: {e}, retrying in {delay} sec ...")
                    time.sleep(delay)
            raise sqlite3.Error("Could not perform the required query")
        return inner
    return outer


@try_to_query_db(3, 2)
def query() -> None:
    conn = sqlite3.connect("006.db")
    cursor = conn.cursor()
    q = "SELECT * FROM STUDENT"
    contents = cursor.execute(q).fetchall()
    print(contents)


def main():
    query()


if __name__ == "__main__":
    main()
