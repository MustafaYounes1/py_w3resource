"""

Write a Python program to create a 'Balanced' Binary Search Tree (BST) using an array of elements where array elements
are sorted in ascending order (see "001.png"). And finally apply pre-order traversal on the tree.

[1, 2, 3, 4, 5, 6, 7]   ->  [4, 2, 1, 3, 6, 5, 7]

"""

from dataclasses import dataclass
from typing import Self


@dataclass
class Node:
    """A node in a BST"""
    val: ...
    left: Self | None = None  # a pointer to the left child
    right: Self | None = None  # a pointer to the right child
    count: int = 1  # a counter to be incremented when adding duplicate values in the BST


def dfs(node: Node, traversal_type: str = "in-order") -> list[...]:
    """Apply depth-first-search to traverse the BST starting from a specific using a specific traversal type"""
    res = []

    if node is None:
        return res

    if traversal_type == "pre-order":
        res += [node.val for _ in range(node.count)]
        res += dfs(node.left, traversal_type)
        res += dfs(node.right, traversal_type)

    elif traversal_type == "in-order":
        res += dfs(node.left, traversal_type)
        res += [node.val for _ in range(node.count)]
        res += dfs(node.right, traversal_type)

    elif traversal_type == "post-order":
        res += dfs(node.left, traversal_type)
        res += dfs(node.right, traversal_type)
        res += [node.val for _ in range(node.count)]

    else:
        raise ValueError(f"Unexpected traversal type: {traversal_type}. "
                         "Expected values: {'in-order', 'pre-order', 'post-order'}")

    return res


class BST:
    """A Binary Search Tree"""
    def __init__(self):
        self.__root: Node | None = None

    @property
    def root(self) -> Node:
        return self.__root

    def insert(self, node_val: ...) -> None:
        """Insert a node to the BST"""
        if self.__root is None:
            self.__root = Node(node_val)

        else:
            self._insert(self.__root, node_val)

    def _insert(self, node: Node, node_val: ...) -> None:
        """Insert logic"""

        # if the current node value is bigger than the new node's value -> go left
        if node_val < node.val:
            if node.left is None:
                node.left = Node(node_val)
            else:
                self._insert(node.left, node_val)

        # if the current node value is less than the new node's value -> go right
        elif node_val > node.val:
            if node.right is None:
                node.right = Node(node_val)
            else:
                self._insert(node.right, node_val)

        # if the current node value equals to the new node's value -> increment the current node's count
        else:
            node.count += 1


def sorted_list_to_balanced_bst(lst: list[...]) -> BST:
    """Create a binary search tree from a sorted list"""
    bst = BST()

    def helper(ll: list[...]) -> None:
        """Recursively bisect the array in order to get a balanced BST"""
        if not ll:
            return

        mid = len(ll) // 2
        bst.insert(ll[mid])

        helper(ll[:mid])    # apply on the left half
        helper(ll[mid+1:])  # apply on the right half

    helper(lst)
    return bst


def main():
    lst = [1, 2, 3, 4, 5, 6, 7]
    bst = sorted_list_to_balanced_bst(lst)

    print(dfs(bst.root, "pre-order"))


if __name__ == "__main__":
    main()
