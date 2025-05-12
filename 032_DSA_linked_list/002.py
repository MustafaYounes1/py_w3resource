"""

Write a Python program to find the size of a singly linked list.

ll = LinkedList()

ll.add("PHP")
ll.add("Python")
ll.add("C#")
ll.add("C++")
ll.add("Java")

print(len(ll))      =>  5

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

    def __len__(self) -> int:
        """Return the size of the linked list"""
        return self.__count


def main():
    ll = LinkedList()

    ll.add("PHP")
    ll.add("Python")
    ll.add("C#")
    ll.add("C++")
    ll.add("Java")

    print(len(ll))


if __name__ == "__main__":
    main()
