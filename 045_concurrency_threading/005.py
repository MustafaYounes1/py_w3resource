"""

Write a Python program to implement a multi-threaded merge sort algorithm.

"""

from concurrent.futures import ThreadPoolExecutor
from heapq import merge
import logging
import random
import threading
import time


logging.basicConfig(
    format="%(asctime)s %(message)s",
    datefmt="%H:%M:%S",
    level=logging.INFO
)


def merge_sort(lst: list[int], reverse: bool = False) -> list[int]:
    """single-threaded implementation"""
    logging.debug(f"{threading.current_thread().name} is sorting ...")

    if len(lst) <= 1:
        logging.debug(f"{threading.current_thread().name} is done ...")
        return lst

    # split and apply merge sort on each half
    mid = len(lst) // 2
    left = merge_sort(lst[:mid], reverse)
    right = merge_sort(lst[mid:], reverse)

    # apply the merge
    res = list(merge(left, right, reverse=reverse))

    logging.debug(f"{threading.current_thread().name} is done ...")

    return res


def mt_merge_sort(lst: list[int], reverse: bool = False, n_threads: int = 5) -> list[int]:
    """multithreaded implementation"""
    size = len(lst) // n_threads
    pool = [lst[_: _ + size] for _ in range(0, len(lst), size)]

    with ThreadPoolExecutor(max_workers=n_threads, thread_name_prefix="thread") as executor:
        res = executor.map(lambda b: merge_sort(b, reverse), pool)

    return list(merge(*res, reverse=reverse))


def main():
    lst = [random.randint(-100, 100) for _ in range(1000)]

    s = time.perf_counter()
    r1 = merge_sort(lst)
    logging.info(f"single-threaded took: {time.perf_counter() - s:.3f}")

    s = time.perf_counter()
    r2 = mt_merge_sort(lst)
    logging.info(f"multithreaded took: {time.perf_counter() - s:.3f}")

    assert sorted(lst) == r1 == r2


if __name__ == "__main__":
    main()
