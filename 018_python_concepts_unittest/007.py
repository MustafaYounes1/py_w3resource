"""

Write a Python unit test program to check if a function handles multi-threading correctly.

You should create 5 threads with each one looping through the range (1, 100_0000) and incrementing a counter for each
loop, start the threads, and join them all, and at the end your test unit should assert that all threads are dead.

"""

import threading
import unittest


def increment_counter() -> None:
    c = 0
    for _ in range(100_000):
        c += 1


class TestMultiThreading(unittest.TestCase):
    """A unit test to test multithreading"""
    def test_on_five_threads(self):
        """Create five threads and assert they are working correctly"""
        threads = []

        for _ in range(5):
            _ = threading.Thread(target=increment_counter)
            threads.append(_)
            _.start()

        for _ in threads:
            _.join()

        for _ in threads:
            self.assertFalse(_.is_alive())


if __name__ == "__main__":
    unittest.main(verbosity=2)
