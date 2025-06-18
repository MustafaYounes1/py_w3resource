"""

Write a Python program that implements a coroutine to fetch data from two different URLs simultaneously using the
"aiohttp" library.

Note: the URLs can be found in "004.txt"

"""

import aiohttp
import asyncio
from pathlib import Path
import time


_URL_SRC = "004.txt"


async def download_all_sites(urls: list[str]) -> None:
    # The tasks can share the session because they’re all running on the same thread. There’s no way one task could
    # interrupt another while the session is in a bad state (Async IO == single-threaded single-process design).
    async with aiohttp.ClientSession() as session:
        tasks = [download_site(url, session) for url in urls]
        await asyncio.gather(*tasks, return_exceptions=True)


async def download_site(url: str, session: aiohttp.ClientSession) -> None:
    async with session.get(url) as response:
        bytes_ = await response.read()
        print(f"Downloaded {len(bytes_):,} bytes from {url}")


async def main():
    assert Path(_URL_SRC).is_file(), f"{_URL_SRC} doesn't exist"

    with open(_URL_SRC, "r") as file:
        urls = [url.strip() for url in file.readlines()]

    s = time.perf_counter()

    await download_all_sites(urls)

    print(f"Downloaded all sites in {time.perf_counter() - s:.3f} sec")


if __name__ == "__main__":
    asyncio.run(main())
