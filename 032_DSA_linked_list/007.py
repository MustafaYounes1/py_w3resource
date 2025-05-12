"""

Write a Python program to create a doubly linked list, append some items and iterate through the list forwards and
backwards.

ll = DoublyLinkedList()

ll.add("PHP")
ll.add("Python")
ll.add("C#")
ll.add("C++")
ll.add("Java")

print(len(ll))          =>  5
print(ll.values)        =>  ['PHP', 'Python', 'C#', 'C++', 'Java']
print(ll.r_values)      =>  ['Java', 'C++', 'C#', 'Python', 'PHP']

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

    @property
    def values(self) -> list[...]:
        """Forward pass through the linked list: head -> tail"""
        res, curr_node = [], self.__head

        while curr_node is not None:
            res.append(curr_node.val)
            curr_node = curr_node.next

        return res

    @property
    def r_values(self) -> list[...]:
        """Backward pass through the linked list: tail -> head"""
        res, curr_node = [], self.__tail

        while curr_node is not None:
            res.append(curr_node.val)
            curr_node = curr_node.previous

        return res


def main():
    ll = DoublyLinkedList()

    ll.add("PHP")
    ll.add("Python")
    ll.add("C#")
    ll.add("C++")
    ll.add("Java")

    print(len(ll))
    print(ll.values)
    print(ll.r_values)


if __name__ == "__main__":
    main()
