"""

Write a Python program to implement a multi-threaded quicksort algorithm.

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


def quick_sort(lst: list[int], reverse: bool = False) -> list[int]:
    """single-threaded implementation (pivot chosen as the last element)"""
    logging.debug(f"{threading.current_thread().name} is sorting ...")

    if len(lst) <= 1:
        logging.debug(f"{threading.current_thread().name} is done ...")
        return lst

    pvt, left, right = lst[-1], [], []

    # place the pivot into its right position
    for _ in lst[:-1]:
        if [_ < pvt, _ >= pvt][reverse]:
            left.append(_)
        else:
            right.append(_)

    res = quick_sort(left, reverse) + [pvt] + quick_sort(right, reverse)

    logging.debug(f"{threading.current_thread().name} is done ...")

    return res


def mt_quick_sort(lst: list[int], reverse: bool = False, n_threads: int = 5) -> list[int]:
    """multithreaded implementation (pivot chosen as the last element)"""
    size = len(lst) // n_threads
    pool = [lst[_: _ + size] for _ in range(0, len(lst), size)]

    with ThreadPoolExecutor(max_workers=n_threads, thread_name_prefix="thread") as executor:
        res = executor.map(lambda b: quick_sort(b, reverse), pool)

    return list(merge(*res, reverse=reverse))


def main():
    lst = [random.randint(-100, 100) for _ in range(1000)]

    s = time.perf_counter()
    r1 = quick_sort(lst)
    logging.info(f"single-threaded took: {time.perf_counter() - s:.3f}")

    s = time.perf_counter()
    r2 = mt_quick_sort(lst)
    logging.info(f"multithreaded took: {time.perf_counter() - s:.3f}")

    assert sorted(lst) == r1 == r2


if __name__ == "__main__":
    main()
