"""

Write a Python program to check whether a given binary tree is a valid binary search tree (BST) or not.

In a binary search tree (BST):
    * The left subtree of a node contains only nodes with keys less than the node's key.
    * The right subtree of a node contains only nodes with keys greater than the node's key.
    * Both the left and right subtrees must also be binary search trees.

See "003.png" for example inputs

"""

from dataclasses import dataclass
from itertools import pairwise
from typing import Self


@dataclass
class Node:
    """A node in a BST"""
    val: ...
    left: Self | None = None  # a pointer to the left child
    right: Self | None = None  # a pointer to the right child


def dfs(node: Node, traversal_type: str = "in-order") -> list[...]:
    """Apply depth-first-search to traverse the BST starting from a specific using a specific traversal type"""
    res = []

    if node is None:
        return res

    if traversal_type == "pre-order":
        res.append(node.val)
        res += dfs(node.left, traversal_type)
        res += dfs(node.right, traversal_type)

    elif traversal_type == "in-order":
        res += dfs(node.left, traversal_type)
        res.append(node.val)
        res += dfs(node.right, traversal_type)

    elif traversal_type == "post-order":
        res += dfs(node.left, traversal_type)
        res += dfs(node.right, traversal_type)
        res.append(node.val)

    else:
        raise ValueError(f"Unexpected traversal type: {traversal_type}. "
                         "Expected values: {'in-order', 'pre-order', 'post-order'}")

    return res


def validate_bst(root: Node) -> bool:
    """Validate whether the given root node forms a valid BST"""
    # apply in-order traverse the binary search tree
    in_order_nodes = dfs(root, "in-order")

    # the nodes should be sorted in ascending order if the tree satisfies BST properties
    for a, b in pairwise(in_order_nodes):
        if a > b:
            return False

    return True


def main():
    bsts = [
        Node(2, Node(1), Node(3)),
        Node(1, Node(2), Node(3)),
    ]

    for _ in bsts:
        print(validate_bst(_))


if __name__ == "__main__":
    main()
