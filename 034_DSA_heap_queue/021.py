"""

Write a Python program to create a priority queue, add -1, -2, -3 to the stack, and get them one by one.

-3 -2 -1

"""

from queue import PriorityQueue


def main():
    q = PriorityQueue()

    for _ in range(-1, -4, -1):
        q.put_nowait(_)

    while not q.empty():
        print(q.get_nowait(), end=" ")


if __name__ == "__main__":
    main()
