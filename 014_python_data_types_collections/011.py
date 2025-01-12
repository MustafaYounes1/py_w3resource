"""

Write a Python program that copies a deque object and verifies shallow copying.
The contents of the original deque are: [1, 3, 5, 7, 9]

[The new deque is a new object with new id]
d1 id: 2551964308224
d2 id: 2551964308464

[The new deque holds references to the items found in the original deque, hence the same id of the elements]
d1 element id: 140716466553640
d2 element id: 140716466553640

"""

from collections import deque


def main():
    d1 = deque([1, 3, 5, 7, 9])
    d2 = d1.copy()

    print(f"d1 id: {id(d1)}")
    print(f"d2 id: {id(d2)}")

    print(f"d1 fist element id: {id(d1[0])}")
    print(f"d2 fist element id: {id(d2[0])}")


if __name__ == "__main__":
    main()
