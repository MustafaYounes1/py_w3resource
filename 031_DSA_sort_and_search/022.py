"""

Write a Python program to sort a list of elements using Tree sort.

Tree sort is a sorting algorithm that builds a Binary Search Tree (BST) from the elements of the array to be sorted
and then performs an in-order traversal of the BST to get the elements in sorted order.

Tree sort uses the properties of BST, where each node has at most two children, referred to as the left and right child.
For any given node:
    * The left child's value is less than the node's value.
    * The right child's value is greater than the node's value.

Tree Sort involves two main steps:
    * Insertion: Insert all elements into the BST.
    * Traversal: Perform an in-order traversal of the BST to extract the elements in sorted order.
        The in-order traversal function will visit all nodes of the BST in sorted order and collect the elements.


Best/Average Time Complexity:       O(n * log(n))
                                    Adding one item to a Binary Search tree on average takes O(log n) time. Therefore,
                                    adding n items will take O(n log n) time

Worst Time Complexity:              O(n^2)
                                    if the tree becomes unbalanced (e.g., if the input array is already sorted).

[14, 46, 43, 27, 57, 41, 45, 21, 70]

Ascending order:    [14, 21, 27, 41, 43, 45, 46, 57, 70]
Descending order:   [70, 57, 46, 45, 43, 41, 27, 21, 14]

"""

from dataclasses import dataclass
from typing import Self


@dataclass
class Node:
    """A class that represents a node in a Binary Tree"""
    value: ...
    count: int = 1  # to handle repeated values in the list to be sorted
    left: None | Self = None
    right: None | Self = None


class BST:
    """A class that represents a Binary Search Tree"""
    def __init__(self):
        self.__root: None | Node = None

    @property
    def root(self):
        """Get the root node"""
        return self.__root

    def insert(self, key: ...) -> None:
        """Insert nodes to the BST"""
        if self.__root is None:
            self.__root = Node(key)
        else:
            self.__insert_helper(self.__root, key)


    def __insert_helper(self, node: Node, key: ...) -> None:
        """Insertion logic"""
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self.__insert_helper(node.left, key)

        elif key > node.value:
            if node.right is None:
                node.right = Node(key)
            else:
                self.__insert_helper(node.right, key)

        else:
            node.count += 1


def traverse_in_order(node: Node, reverse: bool) -> list[...]:
    """Traverse the BST (starting from a specific node) in order to get the sorted values"""
    res = []

    if node is not None:
        if not reverse:
            res += traverse_in_order(node.left, reverse)
            res += [node.value for _ in range(node.count)]
            res += traverse_in_order(node.right, reverse)
        else:
            res += traverse_in_order(node.right, reverse)
            res += [node.value for _ in range(node.count)]
            res += traverse_in_order(node.left, reverse)

    return res


def tree_sort(lst: list[...], reverse: bool = False) -> list[...]:
    """An implementation of tree sort"""
    bst = BST()

    # Build the binary search tree
    for _ in lst:
        bst.insert(_)

    # return the sorted list
    return traverse_in_order(bst.root, reverse)


def main():
    lst = [14, 46, 43, 27, 57, 41, 45, 21, 70]

    print(tree_sort(lst, False))
    print(tree_sort(lst, True))


if __name__ == "__main__":
    main()
