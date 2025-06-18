"""

Write a Python program that performs concurrent HTTP requests using threads.
Note:   URLs can be found in "002.txt"
        Use requests to download contents from the URLs

"""

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import requests
import threading
import time


_URL_SRC = "002.txt"

_THREAD_LOCAL_S = threading.local()  # requests.Session isn't threadsafe -> needs to be protected -> one possible solution
# is the thread-local storage, it resembles a global variable but is specific to each individual thread. This object
# takes care of separating accesses from different threads to its attributes.


def get_thread_session():
    """
    When get_session_for_thread() is called, the session it looks up is specific to the particular thread on which it’s
    running. So each thread will create a single session the first time it calls get_session_for_thread() and then will
    use that session on each subsequent call throughout its lifetime.
    """
    if not hasattr(_THREAD_LOCAL_S, "session"):
        _THREAD_LOCAL_S.session = requests.Session() # creating a Session object allows the library to retain state
        # across requests and reuse the connection to speed things up.

    return _THREAD_LOCAL_S.session


def download(url: str) -> None:
    s = time.perf_counter()
    session = get_thread_session()

    with session.get(url) as response:
        cnt = response.content

    elapsed = time.perf_counter() - s
    print(f"{threading.current_thread().name} downloaded {len(cnt):,} bytes from {url} in {elapsed:.3f} sec")


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
