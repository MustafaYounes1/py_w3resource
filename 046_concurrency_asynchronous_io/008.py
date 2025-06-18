"""

Write a Python program that uses asyncio queues to simulate a producer-consumer scenario with multiple producers and a
single consumer.

"""

import asyncio
from itertools import repeat
import os
import random
import time
from typing import Literal


random.seed(44)

_ANSI_RST = "\033[0m"

_ANSI_CLR_CODES = [
     "\033[31m", # red
     "\033[32m", # green
     "\033[33m", # orange
     "\033[34m", # blue
     "\033[35m", # purple
     "\033[36m", # cyan
     "\033[37m", # light-grey
     "\033[90m", # darkgrey
     "\033[91m", # light-red
     "\033[92m", # light-green
     "\033[93m", # yellow
     "\033[94m", # lightblue
     "\033[95m", # pink
     "\033[96m", # light-cyan
]


def get_ansi(name: int, caller: Literal["p", "c"]) -> str:
    """ANSI codes for colorful printings"""
    mid = len(_ANSI_CLR_CODES) // 2

    if caller == "p":
        colors = _ANSI_CLR_CODES[:mid]

    elif caller == "c":
        colors = _ANSI_CLR_CODES[mid:]

    else:
        raise ValueError

    return colors[name % len(_ANSI_CLR_CODES)]


async def make_item(size: int = 5) -> str:
    """Make random bytes object of a predefined size and get its hex"""
    return os.urandom(size).hex(sep=":")


async def rand_sleep(name: str, ansi_clr: str) -> None:
    """Random asynchronous sleep"""
    d = random.randint(0, 10)
    print(ansi_clr + f"{name} sleeping for {d} sec" + _ANSI_RST)
    await asyncio.sleep(d)


async def produce(name: int, queue: asyncio.Queue[tuple[str, float]]) -> None:
    """Production logic"""
    ansi_clr = get_ansi(name, "p")
    n = random.randint(0, 10)
    print(ansi_clr + f"[+] Producer {name} will produce {n} items" + _ANSI_RST)

    # simulate a synchronous loop for each producer
    for _ in repeat(None, n):
        await rand_sleep(f"[+] Producer {name}", ansi_clr)  # simulate heavy production code
        i = await make_item()  # get the produced item
        t = time.perf_counter()  # ts of the production
        await queue.put((i, t))  # put the produced item along with the production timestamp
        print(ansi_clr + f"[+] Producer {name} added <{i}> to the queue." + _ANSI_RST)


async def consume(name: int, queue: asyncio.Queue[tuple[str, float]]) -> None:
    """Consuming logic"""
    ansi_clr = get_ansi(name, "c")

    while True:
        await rand_sleep(f"[-] Consumer {name}", ansi_clr)  # simulate some heavy consumption code
        i, t = await queue.get()  # get an item from the queue
        now = time.perf_counter()
        print(ansi_clr + f"[-] Consumer {name} got element <{i}> from the queue in {now - t:.3f} sec" + _ANSI_RST)
        queue.task_done()  # signals to the queue that this specific work item has been processed. If a join() is
        # currently blocking, it will resume when all items have been processed (meaning that a task_done() call was
        # received for every item that had been put() into the queue).


async def main():
    n_producers, n_consumers = 3, 1

    queue = asyncio.Queue()

    producers = [asyncio.create_task(produce(idx, queue)) for idx in range(n_producers)]
    consumers = [asyncio.create_task(consume(idx, queue)) for idx in range(n_consumers)]

    await asyncio.gather(*producers)

    await queue.join()  # Block until all items in the queue have been received and processed. The count of unfinished
    # tasks goes up whenever an item is added to the queue. The count goes down whenever a consumer coroutine calls
    # task_done() to indicate that the item was retrieved and all work on it is complete. When the count of unfinished
    # tasks drops to zero, join() unblocks. It implicitly awaits consumers, too.

    for c in consumers:
        c.cancel()


if __name__ == "__main__":
    asyncio.run(main())
