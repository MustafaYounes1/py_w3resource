"""

Write a Python program to delete a node with the given node_val in a given binary search tree (BST).
Note: Search for a node to remove. If the node is found, delete the node.

bst = BST()

bst.insert(13)
bst.insert(7)
bst.insert(3)
bst.insert(8)
bst.insert(15)
bst.insert(14)
bst.insert(19)
bst.insert(18)

print(dfs(bst.root, "in-order"))    =>  [3, 7, 8, 13, 14, 15, 18, 19]

bst.delete(8)
print(dfs(bst.root, "in-order"))    =>  [3, 7, 13, 14, 15, 18, 19]

bst.delete(19)
print(dfs(bst.root, "in-order"))    =>  [3, 7, 13, 14, 15, 18]

bst.delete(13)
print(dfs(bst.root, "in-order"))    =>  [3, 7, 14, 15, 18]

bst.delete(100)
print(dfs(bst.root, "in-order"))    =>  [3, 7, 14, 15, 18]

"""

from dataclasses import dataclass
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

    def delete(self, node_val: ...) -> None:
        """Delete a node from the BST"""
        self.__root = self._delete(self.__root, node_val)

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

        # if the current node value equals to the new node's value -> do nothing (unique values)
        else:
            pass

    def _delete(self, node: Node | None, node_val: ...) -> Node | None:
        """Delete logic"""

        # To delete a node, we must first search the BST to find it

        # if the node in the current call is None -> do nothing
        if node is None:
            return None

        # if node_val to be searched is smaller than the current node value -> keep looking in the left subtree
        elif node_val < node.val:
            node.left = self._delete(node.left, node_val)

        # if node_val to be searched is larger than the current node value -> keep looking in the right subtree
        elif node_val > node.val:
            node.right = self._delete(node.right, node_val)

        # the node with the node_val to be searched was found
        else:
            # the node has one child: a right child
            # connect the parent node (from the previous function call) of the node you want to remove to that child node.
            if node.left is None:
                return node.right

            # the node has one child: a left child
            # connect the parent node (from the previous function call) of the node you want to remove to that child node.
            elif node.right is None:
                return node.left

            # the node has two children
            # Find the node's inorder successor, i.e., the node that comes after it if we were to do in-order traversal
            # which will always be a leaf node that has the smallest value larger than the current node.
            # The in-order successor value would be written as the new value of the node to be removed
            # And finally, the inorder successor (a leaf node) would be deleted.
            else:
                # we can find the in-order successor by applying dfs with in-order traversal starting from the right
                # child -> the first value to be returned would be the in-order successor
                in_order_successor = dfs(node.right, "in-order")[0]

                node.val = in_order_successor  # Replace the node value with the inorder successor

                # Remove the inorder successor (a leaf node) from the BST
                node.right = self._delete(node.right, in_order_successor)

        return node


def main():
    bst = BST()

    bst.insert(13)
    bst.insert(7)
    bst.insert(3)
    bst.insert(8)
    bst.insert(15)
    bst.insert(14)
    bst.insert(19)
    bst.insert(18)

    print(dfs(bst.root, "in-order"))

    bst.delete(8)
    print(dfs(bst.root, "in-order"))

    bst.delete(19)
    print(dfs(bst.root, "in-order"))

    bst.delete(13)
    print(dfs(bst.root, "in-order"))

    bst.delete(100)
    print(dfs(bst.root, "in-order"))


if __name__ == "__main__":
    main()
