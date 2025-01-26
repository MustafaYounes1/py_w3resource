"""

Write a Python program that implements a decorator to measure the memory usage of a function.
    Hint: use 'tracemalloc' to trace memory blocks allocated by Python.
    Implement a function that would calculate the factorial of number and trace its memory allocations, print the
    top 5 statistics of the memory allocations grouped by the filename and the line number

res = factorial(3)

factorial memory usage:
D:\\learn\\python\\w3resource\\021_python_concepts_decorator\\010.py:23: size=128 B, count=2, average=64 B
D:\\learn\\python\\w3resource\\021_python_concepts_decorator\\010.py:42: size=64 B, count=1, average=64 B
factorial memory usage:
D:\\learn\\python\\w3resource\\021_python_concepts_decorator\\010.py:42: size=64 B, count=1, average=64 B
D:\\learn\\python\\w3resource\\021_python_concepts_decorator\\010.py:23: size=64 B, count=1, average=64 B
C:\\Users\\muyo\\anaconda3\\envs\\py_w3resource\\Lib\\tracemalloc.py:485: size=64 B, count=1, average=64 B
C:\\Users\\muyo\\anaconda3\\envs\\py_w3resource\\Lib\\tracemalloc.py:484: size=64 B, count=1, average=64 B
C:\\Users\\muyo\\anaconda3\\envs\\py_w3resource\\Lib\\tracemalloc.py:558: size=56 B, count=1, average=56 B
factorial memory usage:
C:\\Users\\muyo\\anaconda3\\envs\\py_w3resource\\Lib\\tracemalloc.py:193: size=288 B, count=6, average=48 B
C:\\Users\\muyo\\anaconda3\\envs\\py_w3resource\\Lib\\tracemalloc.py:558: size=160 B, count=3, average=53 B
C:\\Users\\muyo\\anaconda3\\envs\\py_w3resource\\Lib\\tracemalloc.py:485: size=128 B, count=2, average=64 B
C:\\Users\\muyo\\anaconda3\\envs\\py_w3resource\\Lib\\tracemalloc.py:484: size=128 B, count=2, average=64 B
factorial memory usage:
C:\\Users\\muyo\\anaconda3\\envs\\py_w3resource\\Lib\\tracemalloc.py:558: size=448 B, count=9, average=50 B
C:\\Users\\muyo\\anaconda3\\envs\\py_w3resource\\Lib\\tracemalloc.py:485: size=128 B, count=2, average=64 B
C:\\Users\\muyo\\anaconda3\\envs\\py_w3resource\\Lib\\tracemalloc.py:484: size=128 B, count=2, average=64 B
D:\\learn\\python\\w3resource\\021_python_concepts_decorator\\010.py:29: size=56 B, count=1, average=56 B

Result: 6

"""

import tracemalloc
from typing import Callable


def trace_memory(func: Callable[..., ...]) -> Callable[..., ...]:
    def wrapper(*args, **kwargs) -> ...:
        # Start tracing Python memory allocations
        tracemalloc.start()

        res = func(*args, **kwargs)

        # Take a snapshot of traces of memory blocks allocated by Python
        snapshot = tracemalloc.take_snapshot()

        # Get statistics as a sorted list of statistics on memory allocations. instances grouped by 'lineno'
        # (filename and line number)
        top_results = snapshot.statistics("lineno")

        print(f"{func.__name__} memory usage: ")
        for _ in top_results[:5]:
            print(_)

        return res

    return wrapper


@trace_memory
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    res = factorial(3)
    print(f"Result: {res:,}")


if __name__ == "__main__":
    main()
