"""

Write a Python program that implements a decorator to enforce rate limits on a function.
    Limits the number of function calls within a specified time period.

"""

import time
from typing import Callable


def limit_api_calls(n_calls: int, period: int | float) -> Callable[..., ...]:
    def outer(func: Callable[..., ...]) -> Callable[..., ...]:
        curr_n_calls = 0
        t = time.time()

        def inner(*args, **kwargs) -> ...:
            nonlocal curr_n_calls, t
            elapsed = time.time() - t

            if elapsed >= period:
                curr_n_calls = 0  # reset the number of calls
                t = time.time()  # reset the start of the time frame

            if curr_n_calls >= n_calls:
                raise PermissionError(f"The rate limit for {func.__name__} was exceeded [{n_calls} in {period} sec]")

            res = func(*args, **kwargs)
            curr_n_calls += 1

            return res

        return inner
    return outer


@limit_api_calls(50, 0.01)
def do_nothing() -> None:
    ...


def main():
    called = 0

    try:
        for _ in range(100):
            do_nothing()
            called += 1

    except PermissionError as e:
        print(e)

    print(f"Called the API {called} times")


if __name__ == "__main__":
    main()
