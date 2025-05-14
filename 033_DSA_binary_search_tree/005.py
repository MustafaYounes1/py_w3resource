"""

Write a Python program to find the kth smallest/largest element in a given binary search tree.

bst = BST()

bst.insert(20)
bst.insert(8)
bst.insert(22)
bst.insert(4)
bst.insert(12)
bst.insert(10)
bst.insert(14)

print(dfs(bst.root, "in-order"))        =>  [4, 8, 10, 12, 14, 20, 22]

print(bst.kth(1, "smallest"))           => 4
print(bst.kth(2, "smallest"))           => 8
print(bst.kth(3, "smallest"))           => 10
print(bst.kth(6, "smallest"))           => 20
print(bst.kth(100, "smallest"))         => None

print(bst.kth(1, "largest"))            => 22
print(bst.kth(4, "largest"))            => 12
print(bst.kth(3, "largest"))            => 14
print(bst.kth(7, "largest"))            => 4
print(bst.kth(100, "largest"))          => None

"""

from dataclasses import dataclass
from typing import Literal, Self


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

    def kth(self, k: int, order: Literal["smallest", "largest"] = "smallest") -> ...:
        """return the kth smallest/largest element in a BST or None if the bst has fewer elements"""
        assert k > 0, "expected non-zero positive k"

        if order not in ("smallest", "largest"):
            raise ValueError("Unrecognized order - possible values: ('smallest', 'largest')")

        count, res = 0, None

        def helper(node: Node):
            """Apply in-order dfs traversal in the BST until the kth smallest element has been found"""
            nonlocal count, res

            # if the current node is None -> do nothing
            if not node:
                return

            # in-order traversal #
            # kth smallest:     left -> node -> right
            # kth largest:      right -> node -> left

            # keep moving left_smallest/right_largest until reaching a node with no left child
            if order == "smallest":
                helper(node.left)
            else:
                helper(node.right)

            # reached a node of interest, i.e., one smallest/largest value
            count += 1

            # if the kth element was reached -> record it
            if count == k:
                res = node.val

            # while kth element hasn't been found -> continue searching
            if count < k:
                if order == "smallest":
                    helper(node.right)
                else:
                    helper(node.left)

        helper(self.__root)

        return res


def main():
    bst = BST()

    bst.insert(20)
    bst.insert(8)
    bst.insert(22)
    bst.insert(4)
    bst.insert(12)
    bst.insert(10)
    bst.insert(14)

    print(dfs(bst.root, "in-order"))

    print(bst.kth(1, "smallest"))
    print(bst.kth(2, "smallest"))
    print(bst.kth(3, "smallest"))
    print(bst.kth(6, "smallest"))
    print(bst.kth(100, "smallest"))

    print(bst.kth(1, "largest"))
    print(bst.kth(4, "largest"))
    print(bst.kth(3, "largest"))
    print(bst.kth(7, "largest"))
    print(bst.kth(100, "largest"))


if __name__ == "__main__":
    main()
