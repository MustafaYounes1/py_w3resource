"""

Write a Python program that creates two threads to find and print even and odd numbers from 0 to 1000.

"""

from itertools import islice
import logging
import threading
import time
from typing import Iterator


_RANGE = range(0, 1001)
_LOG_LVL = logging.INFO

logging.basicConfig(
    format="%(asctime)s: %(message)s",
    datefmt="%H:%M:%S",
    level=_LOG_LVL,
)


def find(it: Iterator[int], evens: list[int], odds: list[int]) -> None:
    for n in it:
        if n % 2 == 0:
            logging.debug(f"{threading.current_thread().name} found an even number")
            evens.append(n) # list.append is thread-safe (atomic operation) -> no need for locking
        else:
            logging.debug(f"{threading.current_thread().name} found an odd number")
            odds.append(n) # list.append is thread-safe (atomic operation) -> no need for locking


def find_with_two_threads() -> tuple[list[int], list[int]]:
    """Multithreaded implementation (2 threads)"""
    evens, odds = [], []

    t1 = threading.Thread(target=find, args=(islice(_RANGE, len(_RANGE) // 2), evens, odds))
    t2 = threading.Thread(target=find, args=(islice(_RANGE, len(_RANGE) // 2, None), evens, odds))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    return evens, odds


def sync_find() -> tuple[list[int], list[int]]:
    """Single-threaded implementation"""
    evens, odds = [], []
    it = iter(_RANGE)

    find(it, evens, odds)

    return evens, odds


def main():
    mt_s = time.perf_counter()
    mt_evens, mt_odds = find_with_two_threads()
    mt_t = time.perf_counter() - mt_s

    s_s = time.perf_counter()
    s_evens, s_odds = sync_find()
    s_t = time.perf_counter() - s_s

    assert set(s_evens) == set(mt_evens) and set(s_odds) == set(mt_odds)

    logging.info(f"Multi-threaded implementation took: {mt_t:.3f} sec")
    logging.info(f"Single-threaded implementation took: {s_t:.3f} sec")
    logging.info(f"Evens: {s_evens}")
    logging.info(f"Odds:  {s_odds}")


if __name__ == "__main__":
    main()
