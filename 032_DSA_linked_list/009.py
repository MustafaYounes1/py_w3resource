"""

Write a Python program to search a specific item in a given doubly linked list and return the index of the element.

Note:
    * Implement both:
        find    -   the search would start from the head
        rfind   -   the search would start from the tail
    * return -1 if the item wasn't found

ll = DoublyLinkedList()

ll.add("PHP")
ll.add("Python")
ll.add("C#")
ll.add("C++")
ll.add("Python")
ll.add("Java")
ll.add("SQL")

print(ll.find("PHP"))       =>  0
print(ll.find("Python"))    =>  1
print(ll.rfind("Python"))   =>  4
print(ll.rfind("SQL"))      =>  6

print(ll.find("Dart"))      =>  -1
print(ll.rfind("HTML"))     =>  -1

"""

from dataclasses import dataclass
from typing import Self


@dataclass
class Node:
    val: ...
    next: Self | None = None  # a pointer to the next node
    previous: Self | None = None  # a pointer to the previous node


class DoublyLinkedList:
    def __init__(self):
        self.__head: Node | None = None  # first node
        self.__tail: Node | None = None  # last node
        self.__count: int = 0

    def add(self, node_val: ...) -> None:
        """Add a node to the end of the list"""
        new_node = Node(node_val)

        if self.__head is None:
            # initially both head and tail are the same node
            self.__head = new_node
            self.__tail = new_node

        else:
            new_node.previous = self.__tail  # the new node's previous node is the previous tail
            self.__tail.next = new_node  # the previous tail's next node is the new node
            self.__tail = new_node  # update the tail

        self.__count += 1

    def __len__(self) -> int:
        return self.__count

    def find(self, item: ...) -> int:
        """LeftSearch for item in liked list and return the index of the first match (-1 if it was not found)"""
        idx, curr_node = 0, self.__head

        while curr_node is not None:
            if curr_node.val == item:
                return idx

            curr_node = curr_node.next
            idx += 1

        return -1

    def rfind(self, item: ...) -> int:
        """RightSearch for item in liked list and return the index of the first match (-1 if it was not found)"""
        idx, curr_node = len(self) - 1, self.__tail

        while curr_node is not None:
            if curr_node.val == item:
                return idx

            curr_node = curr_node.previous
            idx -= 1

        return -1


def main():
    ll = DoublyLinkedList()

    ll.add("PHP")
    ll.add("Python")
    ll.add("C#")
    ll.add("C++")
    ll.add("Python")
    ll.add("Java")
    ll.add("SQL")

    print(ll.find("PHP"))
    print(ll.find("Python"))
    print(ll.rfind("Python"))
    print(ll.rfind("SQL"))

    print(ll.find("Dart"))
    print(ll.rfind("HTML"))


if __name__ == "__main__":
    main()
