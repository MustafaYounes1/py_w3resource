"""

Write a Python program to search a specific item in a singly linked list and return true if the item is found
otherwise return false.

ll = LinkedList()

ll.add("PHP")
ll.add("Python")
ll.add("C#")
ll.add("C++")
ll.add("Java")

print("SQL" in ll)      =>  False
print("C++" in ll)      =>  True

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

    def __contains__(self, item: ...) -> bool:
        """is the item in the linked list?"""
        curr_node = self.__head

        while curr_node is not None:
            if curr_node.val == item:
                return True
            curr_node = curr_node.next

        return False


def main():
    ll = LinkedList()

    ll.add("PHP")
    ll.add("Python")
    ll.add("C#")
    ll.add("C++")
    ll.add("Java")

    print("SQL" in ll)
    print("C++" in ll)


if __name__ == "__main__":
    main()
