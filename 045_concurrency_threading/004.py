"""

Write a Python program to calculate the factorial of a number using multiple threads.

"""

from concurrent.futures import ThreadPoolExecutor
from itertools import islice
import logging
from math import factorial, prod
import threading
import time


logging.basicConfig(
    format="%(asctime)s %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S"
)


def sync_factorial(n: int) -> int:
    """Single-threaded (iterative) implementation"""
    return prod(range(1, n + 1))


def subseq_prod(seq: tuple[int]) -> int:
    """Find the product of a subsequence in [1, n] using one thread"""
    logging.debug(f"{threading.current_thread().name} started working")
    res = prod(seq)
    logging.debug(f"{threading.current_thread().name} finished working")
    return res


def mt_factorial(n: int, bs: int) -> int:
    """multithreaded implementation"""
    it = iter(range(1, n + 1))

    pool = []

    # batchify the range [1, n] into batches of the predefined size
    while batch := tuple(islice(it, bs)):
        pool.append(batch)

    with ThreadPoolExecutor(max_workers=10, thread_name_prefix="thread") as executor:
        res = executor.map(subseq_prod, pool)

    return prod(res)


def main():
    n, bs = 1000, 200

    s = time.perf_counter()
    r1 = factorial(n)
    logging.info(f"Factorial from math module took: {time.perf_counter() - s:.3f}")

    s = time.perf_counter()
    r2 = sync_factorial(n)
    logging.info(f"Single-threaded iterative implementation took: {time.perf_counter() - s:.3f}")

    s = time.perf_counter()
    r3 = mt_factorial(n, bs)
    assert r1 == r2 == r3
    logging.info(f"Multi-threaded implementation took: {time.perf_counter() - s:.3f}")


if __name__ == "__main__":
    main()
