"""

Write a Python program to delete the first occurrence of an item from a singly linked list.

ll = LinkedList()

ll.add("PHP")
ll.add("Python")
ll.add("C#")
ll.add("PHP")
ll.add("C++")
ll.add("Java")
ll.add("C#")

print(ll.values)        =>  ['PHP', 'Python', 'C#', 'PHP', 'C++', 'Java', 'C#']

ll.delete("PHP")
print(ll.values)        =>  ['Python', 'C#', 'PHP', 'C++', 'Java', 'C#']

ll.delete("C#")
print(ll.values)        =>  ['Python', 'PHP', 'C++', 'Java', 'C#']

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

    def delete(self, item: ...) -> None:
        """Delete the first occurrence of an item in the list"""
        if self.__head is None:
            return

        elif self.__head.val == item:
            self.__head = self.__head.next
            self.__count -= 1

        else:
            curr_node = self.__head

            while curr_node is not None:
                if (curr_node.next is not None) and (curr_node.next.val == item):
                    curr_node.next = curr_node.next.next
                    self.__count -= 1
                    return

                curr_node = curr_node.next

    def __len__(self) -> int:
        return self.__count

    @property
    def values(self) -> list[...]:
        """Return the values of the nodes in the linked list"""
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
    ll.add("PHP")
    ll.add("C++")
    ll.add("Java")
    ll.add("C#")

    print(ll.values)

    ll.delete("PHP")
    print(ll.values)

    ll.delete("C#")
    print(ll.values)


if __name__ == "__main__":
    main()
