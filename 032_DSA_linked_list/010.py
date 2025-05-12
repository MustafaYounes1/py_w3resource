"""

Write a Python program to delete a specific item from a given doubly linked list.

Note:
    * Implement both:
        delete    -  delete the first occurrence of an item
        r_delete   - delete the last occurrence of an item

ll = DoublyLinkedList()

ll.add("PHP")
ll.add("Python")
ll.add("C#")
ll.add("PHP")
ll.add("C++")
ll.add("Java")
ll.add("Python")
ll.add("C#")

print(ll.values)        =>  ['PHP', 'Python', 'C#', 'PHP', 'C++', 'Java', 'Python', 'C#']
print(ll.r_values)      =>  ['C#', 'Python', 'Java', 'C++', 'PHP', 'C#', 'Python', 'PHP']


ll.delete("PHP")
print(ll.values)        =>  ['Python', 'C#', 'PHP', 'C++', 'Java', 'Python', 'C#']
print(ll.r_values)      =>  ['C#', 'Python', 'Java', 'C++', 'PHP', 'C#', 'Python']


ll.r_delete("Python")
print(ll.values)        =>  ['Python', 'C#', 'PHP', 'C++', 'Java', 'C#']
print(ll.r_values)      =>  ['C#', 'Java', 'C++', 'PHP', 'C#', 'Python']


ll.r_delete("C#")
print(ll.values)        =>  ['Python', 'C#', 'PHP', 'C++', 'Java']
print(ll.r_values)      =>  ['Java', 'C++', 'PHP', 'C#', 'Python']


ll.delete("C#")
print(ll.values)        =>  ['Python', 'PHP', 'C++', 'Java']
print(ll.r_values)      =>  ['Java', 'C++', 'PHP', 'Python']

print(len(ll))          =>  4

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

    def delete(self, item: ...) -> None:
        """Delete the first occurrence of the provided item"""
        if self.__head is None:
            return

        elif self.__head.val == item:
            self.__head = self.__head.next

            if self.__head is None:
                self.__tail = None
            else:
                self.__head.previous = None

            self.__count -= 1

        else:
            curr_node = self.__head

            while curr_node is not None:
                if (curr_node.next is not None) and (curr_node.next.val == item):
                    curr_node.next.next.previous = curr_node
                    curr_node.next = curr_node.next.next
                    self.__count -= 1
                    return

                curr_node = curr_node.next

    def r_delete(self, item: ...) -> None:
        """Delete the last occurrence of the provided item"""
        if self.__tail is None:
            return

        elif self.__tail.val == item:
            self.__tail = self.__tail.previous

            if self.__tail is None:
                self.__head = None
            else:
                self.__tail.next = None

            self.__count -= 1

        else:
            curr_node = self.__tail

            while curr_node is not None:
                if (curr_node.previous is not None) and (curr_node.previous.val == item):
                    curr_node.previous.previous.next = curr_node
                    curr_node.previous = curr_node.previous.previous
                    self.__count -= 1
                    return

                curr_node = curr_node.previous

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
    ll.add("PHP")
    ll.add("C++")
    ll.add("Java")
    ll.add("Python")
    ll.add("C#")

    print(ll.values)
    print(ll.r_values)

    print("=" * 25)

    ll.delete("PHP")
    print(ll.values)
    print(ll.r_values)

    print("=" * 25)

    ll.r_delete("Python")
    print(ll.values)
    print(ll.r_values)

    print("=" * 25)

    ll.r_delete("C#")
    print(ll.values)
    print(ll.r_values)

    print("=" * 25)

    ll.delete("C#")
    print(ll.values)
    print(ll.r_values)

    print("=" * 25)

    print(len(ll))


if __name__ == "__main__":
    main()
