"""

Write a Python program to find out whether a queue is empty or not.

"""

from queue import Queue


def main():
    q = Queue()
    print(q.empty())
    q.put_nowait(1)
    print(q.empty())


if __name__ == "__main__":
    main()
