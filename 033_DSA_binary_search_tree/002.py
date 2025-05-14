"""

Write a Python program to find the closest value to a given target value in a given non-empty Binary Search Tree (BST)
of unique values, i.e., the task is to find the node with a minimum absolute difference with the given target value.

bst = BST()

bst.insert(9)
bst.insert(4)
bst.insert(17)
bst.insert(3)
bst.insert(6)
bst.insert(5)
bst.insert(7)
bst.insert(22)
bst.insert(20)

print(dfs(bst.root, "pre-order"))       =>  [9, 4, 3, 6, 5, 7, 17, 22, 20]

print(closest_node(bst, 4))       =>  4
print(closest_node(bst, 18))      =>  17
print(closest_node(bst, 12))      =>  9
print(closest_node(bst, 2))       =>  3

"""

from dataclasses import dataclass
import math
from typing import Self


@dataclass
class Node:
    """A node in a BST"""
    val: int | float
    left: Self | None = None  # a pointer to the left child
    right: Self | None = None  # a pointer to the right child


def dfs(node: Node, traversal_type: str = "in-order") -> list[int | float]:
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


class BST:
    """A Binary Search Tree"""
    def __init__(self):
        self.__root: Node | None = None

    @property
    def root(self) -> Node:
        return self.__root

    def insert(self, node_val: int | float) -> None:
        """Insert a node to the BST"""
        if self.__root is None:
            self.__root = Node(node_val)

        else:
            self._insert(self.__root, node_val)

    def _insert(self, node: Node, node_val: int | float) -> None:
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

        # if the current node value equals to the new node's value -> do nothing (unique values)
        else:
            pass


def naive_closest_node(bst: BST, target_val: int | float) -> int | float:
    """A naive approach that traverses the BST in order and find the node with the minimum absolute difference
    Time Complexity: O(n)"""
    in_order_nodes = dfs(bst.root, "in-order")

    # empty bst
    if not in_order_nodes:
        raise ValueError("Empty binary search tree")
    else:
        return min(in_order_nodes, key=lambda _: abs(_ - target_val))


def closest_node(bst: BST, target_val: int | float) -> int | float:
    """Apply DFS while searching for the closet value in a BST while harnessing the properties of BST
    Time Complexity: O(h) where h is the height of the tree"""
    curr_node, min_d, closest = bst.root, math.inf, None

    # start searching for the closet node
    while curr_node is not None:
        d = abs(curr_node.val - target_val)  # get the absolute difference with the current node

        # if found a smaller abs difference -> update the minimum abs difference and the closest node
        if d < min_d:
            closest, min_d = curr_node.val, d

        # if the current node's value is greater than the target node's value -> continue searching in the left subtree
        if curr_node.val > target_val:
            curr_node = curr_node.left

        # if the current node's value is smaller than the target node's value -> continue searching in the right subtree
        elif curr_node.val < target_val:
            curr_node = curr_node.right

        # if the current node's value equals to the target node's value -> the minimum absolute difference of 0 was
        # found already -> stop the search
        else:
            break

    if closest is None:
        raise ValueError("Empty binary tree")

    return closest


def main():
    bst = BST()

    bst.insert(9)
    bst.insert(4)
    bst.insert(17)
    bst.insert(3)
    bst.insert(6)
    bst.insert(5)
    bst.insert(7)
    bst.insert(22)
    bst.insert(20)

    print(dfs(bst.root, "pre-order"))

    print(closest_node(bst, 4))
    print(closest_node(bst, 18))
    print(closest_node(bst, 12))
    print(closest_node(bst, 2))


if __name__ == "__main__":
    main()
