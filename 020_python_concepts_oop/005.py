"""

Write a Python program to create a class representing a binary search tree. Include methods for:
    1. inserting nodes
    2. traversing the tree depth-first with different orders: (in-order, pre-order, and post-order)
    3. traversing the tree breadth-first
    4. searching for values
    5. find min_val
    6. find max_val
    7. deleting node


bst.insert(8)
bst.insert(3)
bst.insert(1)
bst.insert(6)
bst.insert(7)
bst.insert(10)
bst.insert(14)
bst.insert(4)

in-order traversal      =>  [1, 3, 4, 6, 7, 8, 10, 14]
pre-order traversal     =>  [8, 3, 1, 6, 4, 7, 10, 14]
post-order traversal    =>  [1, 4, 7, 6, 3, 14, 10, 8]

14  in bst      =>  True
34  in bst      =>  False
6   in bst      =>  True
0   in bst      =>  False
8   in bst      =>  True

Minimum value in the bst:  1
Maximum value in the bst: 14

// delete 8 from the BST //
8 in bst: False
In-order:   [1, 3, 4, 6, 7, 10, 14]

"""

from collections import deque
from dataclasses import dataclass
from typing import Self, Union


@dataclass
class Node:
    value: Union[int, float]
    left: Union[Self, None] = None
    right: Union[Self, None] = None


def dfs(node: Node, traversal_type: str = "in_order") -> list:
    """Traverse a tree (starting from a specific node) depth-first in different orders"""
    res = []

    if node is not None:
        if traversal_type == "in_order":
            res += dfs(node.left, traversal_type)
            res.append(node.value)
            res += dfs(node.right, traversal_type)

        elif traversal_type == "pre_order":
            res.append(node.value)
            res += dfs(node.left, traversal_type)
            res += dfs(node.right, traversal_type)

        elif traversal_type == "post_order":
            res += dfs(node.left, traversal_type)
            res += dfs(node.right, traversal_type)
            res.append(node.value)

        else:
            raise ValueError(f"Unexpected traversal type: {traversal_type}. "
                             "Expected values: {'in_order', 'pre_order', 'post_order'}")

    return res


def bfs(node: Node) -> list:
    """Traverse a tree (starting from a specific node) breadth-first (level-order traversal)"""
    res = []

    if node is not None:
        d = deque([node])
        while d:
            n = d.popleft()
            res.append(n.value)

            if n.left is not None:
                d.append(n.left)

            if n.right is not None:
                d.append(n.right)

    return res


class BST:
    """An implementation of a binary search tree"""
    def __init__(self):
        self.__root: Union[None, Node] = None

    @property
    def root(self):
        """Get the root node"""
        return self.__root

    def insert(self, key: int) -> None:
        """Insert a key into the BST"""
        if self.__root is None:
            self.__root = Node(key)

        else:
            self.__insert_helper(self.__root, key)

    def delete(self, key: int) -> None:
        """Delete a key from the BST"""
        self.__root = self.__delete_helper(self.__root, key)

    def __contains__(self, key: int) -> bool:
        """Check whether a given key is in the BST"""
        if self.__root is None:
            return False

        else:
            return self.__in_helper(self.__root, key)

    @property
    def min_val(self) -> Union[int, None]:
        """Return the minimum value in the BST"""
        if self.__root is None:
            return None

        else:
            curr = self.__root
            while curr.left is not None:
                curr = curr.left

            return curr.value

    @property
    def max_val(self) -> Union[int, None]:
        """Return the maximum value in the BST"""
        if self.__root is None:
            return None

        else:
            curr = self.__root
            while curr.right is not None:
                curr = curr.right

            return curr.value

    def __insert_helper(self, node: Node, key: int) -> None:
        """A helper method to recursively insert a key into the right position"""
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

    def __in_helper(self, node: Node, key: int) -> bool:
        """A helper method to recursively check whether a key is in the BST"""
        if node is None:
            return False

        elif node.value == key:
            return True

        elif key < node.value:
            return self.__in_helper(node.left, key)

        else:
            return self.__in_helper(node.right, key)

    def __delete_helper(self, node: Node, key: int) -> Union[Node, None]:
        """A helper method to recursively find the node and delete it without breaking the BST properties"""
        if node is None:
            return None

        elif key < node.value:
            node.left = self.__delete_helper(node.left, key)

        elif key > node.value:
            node.right = self.__delete_helper(node.right, key)

        # the node is found
        else:
            # the node has one child
            if node.left is None:
                return node.right

            elif node.left is None:
                return node.left

            # the node has two children
            else:
                n = dfs(node.right, "in_order")[0]  # Get the inorder successor of that node
                node.value = n  # Replace the node value with the inorder successor
                # Remove the inorder successor from its original position
                node.right = self.__delete_helper(node.right, n)

        return node


def main():
    bst = BST()

    bst.insert(8)
    bst.insert(3)
    bst.insert(1)
    bst.insert(6)
    bst.insert(7)
    bst.insert(10)
    bst.insert(14)
    bst.insert(4)

    print(f"BFS:            {bfs(bst.root)}")
    print(f"DFS In-order:   {dfs(bst.root, traversal_type='in_order')}")
    print(f"DFS Pre-order:  {dfs(bst.root, traversal_type='pre_order')}")
    print(f"DFS Post-order: {dfs(bst.root, traversal_type='post_order')}")

    for _ in (14, 34, 6, 0, 8):
        print(f"{_:2d} in bst: {_ in bst}")

    print(f"Minimum value in the bst: {bst.min_val}")
    print(f"Maximum value in the bst: {bst.max_val}")

    bst.delete(8)
    print(f"{8} in bst: {8 in bst}")
    print(f"DFS In-order:   {dfs(bst.root, traversal_type='in_order')}")


if __name__ == "__main__":
    main()
