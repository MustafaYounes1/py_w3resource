"""

Write a Python program to create a queue, add 0 -> 9, display all the members and the size of the queue.

The size of the queue: 10
0 1 2 3 4 5 6 7 8 9

"""

from queue import Queue


def main():
    q = Queue()

    for _ in range(10):
        q.put_nowait(_)

    print(f"The size of the queue: {q.qsize()}")

    for _ in q.queue:
        print(_, end=" ")


if __name__ == "__main__":
    main()
