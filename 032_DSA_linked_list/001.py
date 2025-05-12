"""

Write a Python program to create a singly linked list, append some items and iterate through the list.

ll = LinkedList()

ll.add("PHP")
ll.add("Python")
ll.add("C#")
ll.add("C++")
ll.add("Java")

print(ll.values)    =>  ['PHP', 'Python', 'C#', 'C++', 'Java']

"""

from dataclasses import dataclass
from typing import Self


@dataclass
class Node:
    val: ...
    next: None | Self = None  # a pointer to the next node


class LinkedList:
    def __init__(self):
        self.__head: Node | None = None

    def add(self, node_val: ...) -> None:
        """Add a node at the end of the linked list"""
        new_node = Node(node_val)

        if self.__head is None:
            self.__head = new_node

        else:
            curr_node = self.__head

            while curr_node.next is not None:
                curr_node = curr_node.next

            curr_node.next = new_node

    @property
    def values(self) -> list[...]:
        res, curr_node = [], self.__head

        while curr_node is not None:
            res.append(curr_node.val)
            curr_node = curr_node.next

        return res


def main():
    ll = LinkedList()

    ll.add("PHP")
    ll.add("Python")
    ll.add("C#")
    ll.add("C++")
    ll.add("Java")

    print(ll.values)


if __name__ == "__main__":
    main()
