"""

Write a Python program to access a specific item in a singly linked list using index value.

ll = LinkedList()

ll.add("PHP")
ll.add("Python")
ll.add("C#")
ll.add("C++")
ll.add("Java")

print(ll[0])        =>  PHP
print(ll[1])        =>  Python
print(ll[4])        =>  Java
print(ll[5])        =>  IndexError: linked list index out of range

"""

from dataclasses import dataclass
from typing import Self


@dataclass
class Node:
    val: ...
    next: Self | None = None  # a pointer to the next node


class LinkedList:
    def __init__(self):
        self.__head: Node | None = None
        self.__count: int = 0

    def add(self, node_val: ...) -> None:
        """Add a node to the end of the list"""
        new_node = Node(node_val)

        if self.__head is None:
            self.__head = new_node

        else:
            curr_node = self.__head

            while curr_node.next is not None:
                curr_node = curr_node.next

            curr_node.next = new_node

        self.__count += 1

    def __getitem__(self, idx: int) -> ...:
        """Access item by index"""
        if idx >= self.__count:
            raise IndexError("linked list index out of range")

        curr_node = self.__head
        for _ in range(idx):
            curr_node = curr_node.next

        return curr_node.val


def main():
    ll = LinkedList()

    ll.add("PHP")
    ll.add("Python")
    ll.add("C#")
    ll.add("C++")
    ll.add("Java")

    print(ll[0])
    print(ll[1])
    print(ll[4])
    print(ll[5])


if __name__ == "__main__":
    main()
