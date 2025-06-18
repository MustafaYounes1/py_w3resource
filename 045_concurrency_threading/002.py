"""

Write a Python program to download multiple files concurrently using threads.
Note:   URLs can be found in "002.txt"
        Use urllib.request to download contents from the URLs

"""

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import threading
import time
from urllib.request import urlopen


_URL_SRC = "002.txt"


def download(url: str) -> None:
    s = time.perf_counter()

    with urlopen(url) as response:
        contents = response.read()

    elapsed = time.perf_counter() - s
    print(f"{threading.current_thread().name} downloaded {len(contents):,} bytes from {url} in {elapsed:.3f} sec")


def main():
    assert Path(_URL_SRC).is_file(), f"{_URL_SRC} doesn't exist"

    with open(_URL_SRC, "r") as file:
        urls = [url.strip() for url in file.readlines()]

    s = time.perf_counter()

    with ThreadPoolExecutor(max_workers=10, thread_name_prefix="thread") as executor:
        executor.map(download, urls)

    print(f"Downloaded all sites in {time.perf_counter() - s:.3f} sec")


if __name__ == "__main__":
    main()
