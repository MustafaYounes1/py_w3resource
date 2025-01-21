"""

Write a Python program to create a class representing a linked list data structure. Include methods for:
    1. inserting nodes (at the beginning, at the end, and at a given index)
    2. updating a node given a certain index
    3. deleting nodes (first node, last node, a node that hold given data (first occurrence), and at a node given index)
    4. check whether a value exists in the linked list
    5. getting the size of the linked list
    6. displaying the linked list data

ll = LinkedList()

ll.insert(0, 'a')
ll.insert(1, 'b')
ll.insert(-1, 'c')
ll.insert(-1, 'e')
ll.insert(3, 'd')

ll          =>  ['a', 'b', 'c', 'd', 'e']
'd' in ll   =>  True

ll.delete(0)
ll.delete(1)
ll.remove('d')

The size of the linked list     =>  2
ll                              =>  ['b', 'e']
'd' in ll                       =>  False

ll.update(0, 'z')

ll                              =>  ['z', 'e']

"""

from dataclasses import dataclass
from typing import Self, Union


@dataclass
class Node:
    data: object
    next: Union[Self, None] = None


class LinkedList:
    def __init__(self):
        self.__head: Union[Node, None] = None

    def insert(self, idx: int, data: object) -> None:
        """
        Insert a node to the linked list at different positions
        @:param idx: the index where to add the node (0 for the head, -1 for the tail, or at a specific index (would
        raise IndexError if the given index exceeds the linked list bounds)
        @:param data: the data that would get stored in the added node
        """
        if idx == 0:
            if self.__head is None:
                self.__head = Node(data)
            else:
                self.__head, self.__head.next = Node(data), self.__head

        elif idx == -1:
            if self.__head is None:
                self.__head = Node(data)
            else:
                curr_node = self.__head

                while curr_node.next is not None:
                    curr_node = curr_node.next

                curr_node.next = Node(data)

        elif idx > 0:
            pos, curr_node = 0, self.__head
            while (pos + 1 < idx) and (curr_node is not None):
                pos += 1
                curr_node = curr_node.next

            if curr_node is None:
                raise IndexError(f"{idx} exceeds the linked list bounds")

            curr_node.next, curr_node.next.next = Node(data), curr_node.next

        else:
            raise IndexError("Trying to insert data at negative indices (except for -1) is not supported")

    def update(self, idx: int, data: object) -> None:
        """
        Update a node at a given index
        @:param idx: the index of the node to be updated (would raise IndexError if the given index is negative or
        exceeds the linked list bounds)
        @:param data: the new data the node would hold
        """
        if idx < 0:
            raise IndexError("Negative indices are not supported for the update operation")

        pos, cur_node = 0, self.__head
        while (pos < idx) and (cur_node is not None):
            pos += 1
            cur_node = cur_node.next

        if cur_node is None:
            raise IndexError(f"{idx} exceeds the linked list bounds")

        cur_node.data = data

    def delete(self, idx: int) -> None:
        """
        Delete a node from the linked list at different positions
        @:param idx: the index where to add the node (0 for the head, -1 for the tail, or at a specific index (would
        raise IndexError if the given exceeds the linked list bounds)
        """
        if self.__head is None:
            raise IndexError("The linked list is empty")

        if idx == 0:
            self.__head = self.__head.next

        elif idx == -1:
            if self.__head.next is None:
                self.__head = None
                return

            curr_node = self.__head
            while (curr_node.next is not None) and (curr_node.next.next is not None):
                curr_node = curr_node.next

            curr_node.next = None

        elif idx > 0:
            pos, curr_node = 0, self.__head
            while (pos + 1 < idx) and (curr_node.next is not None) and (curr_node.next.next is not None):
                pos += 1
                curr_node = curr_node.next

            if (pos + 1 < idx) or (curr_node is None) or (curr_node.next is None):
                raise IndexError(f"{idx} exceeds the linked list bounds")

            curr_node.next = curr_node.next.next

        else:
            raise IndexError("Trying to delete nodes at negative indices (except for -1) is not supported")

    def remove(self, data: object) -> None:
        """
        Remove the first node with the given data from the linked list
        @:param data: The data that is supposed to be stored in the node to be deleted  (would raise a ValueError if
        the value doesn't exist in the linked list)
        """
        if self.__head is None:
            raise ValueError("The linked list is empty")

        if self.__head.data == data:
            self.delete(0)
            return

        curr_node = self.__head
        while (curr_node.next is not None) and (curr_node.next.data != data) and (curr_node.next.next is not None):
            curr_node = curr_node.next

        if (curr_node.next is None) or (curr_node.next.data != data):
            raise ValueError(f"{data} does not exist in the linked list")

        curr_node.next = curr_node.next.next

    def __contains__(self, data: object) -> bool:
        """Check whether an item exists in the linked list"""
        curr_node = self.__head
        while curr_node is not None:
            if curr_node.data == data:
                return True

            curr_node = curr_node.next

        return False

    def __len__(self) -> int:
        """Get the size of the linked list"""
        size, curr_node = 0, self.__head
        while curr_node is not None:
            size += 1
            curr_node = curr_node.next

        return size

    def to_list(self) -> list:
        """Get the linked list data as a list"""
        res, curr_node = [], self.__head
        while curr_node is not None:
            res.append(curr_node.data)
            curr_node = curr_node.next

        return res


def main():
    ll = LinkedList()
    ll.insert(0, 'a')
    ll.insert(1, 'b')
    ll.insert(-1, 'c')
    ll.insert(-1, 'e')
    ll.insert(3, 'd')

    print(ll.to_list())
    print('d' in ll)

    ll.delete(0)
    ll.delete(1)
    ll.remove('d')
    print(f"The size of the linked list: {len(ll)}")
    print(ll.to_list())
    print('d' in ll)

    ll.update(0, 'z')
    print(ll.to_list())


if __name__ == "__main__":
    main()
