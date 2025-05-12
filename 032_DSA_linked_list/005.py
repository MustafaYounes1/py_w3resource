"""

Write a Python program to set a new value of an item in a singly linked list using index value.

ll = LinkedList()

ll.add("PHP")
ll.add("Python")
ll.add("C#")
ll.add("C++")
ll.add("Java")

print(ll[1])        =>  Python
print(ll[4])        =>  Java

ll[1] = "SQL"
ll[4] = "Perl"

print(ll[1])        =>  SQL
print(ll[4])        =>  Perl

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

    def __setitem__(self, key: int, value: ...) -> None:
        """Access a node by its index and set a new value for it"""
        if key >= self.__count:
            raise IndexError("linked list index out of range")

        curr_node = self.__head
        for _ in range(key):
            curr_node = curr_node.next

        curr_node.val = value


def main():
    ll = LinkedList()

    ll.add("PHP")
    ll.add("Python")
    ll.add("C#")
    ll.add("C++")
    ll.add("Java")

    print(ll[1])
    print(ll[4])

    ll[1] = "SQL"
    ll[4] = "Perl"

    print(ll[1])
    print(ll[4])


if __name__ == "__main__":
    main()
