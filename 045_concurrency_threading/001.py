"""

Write a Python program to create 10 threads and print their names.

"""

from concurrent.futures import ThreadPoolExecutor
import threading
import time


def thread_job() -> None:
    print(f"{threading.current_thread().name} started running ..")
    time.sleep(1)  # simulate some work that takes 1 second to complete
    print(f"{threading.current_thread().name} finishing it's job ..")


def main():
    with ThreadPoolExecutor(thread_name_prefix="Thread") as executor:
        for _ in range(10):
            executor.submit(thread_job)


if __name__ == "__main__":
    main()
