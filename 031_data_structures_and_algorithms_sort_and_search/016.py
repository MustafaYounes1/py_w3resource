"""

Write a Python program to sort a list of elements using Heap sort.

In computer science, heapsort (invented by J. W. J. Williams in 1964) is a comparison-based sorting algorithm.
Heapsort can be thought of as an improved selection sort: like that algorithm, it divides its input into a sorted and
an unsorted region, and it interactively shrinks the unsorted region by extracting the largest element and moving that
to the sorted region.

The improvement consists of the use of a heap data structure rather than a linear-time search to find the maximum.
Although somewhat slower in practice on most machines than a well-implemented quicksort, it has the advantage of a more
favorable worst-case O(n log n) runtime.

Heapsort is an in-place algorithm, but it is not a stable sort.

============
Binary Tree
============
A binary tree is a tree data structure in which each parent node can have at most two children.
Each node of a binary tree consists of three items:
    * data item
    * address of left child
    * address of right child

Full Binary Tree: A full Binary tree is a special type of binary tree in which every parent node/internal node has
either two or no children.

Perfect Binary Tree: A perfect binary tree is a type of binary tree in which every internal node has exactly two
child nodes and all the leaf nodes are at the same level.

Complete Binary Tree: A complete binary tree is just like a full binary tree, but with two major differences:
    * All the leaf elements must lean towards the left.
    * The last leaf element might not have a right sibling i.e. a complete binary tree doesn't have to be a full
    binary tree.

=====
Heap
=====
Heap data structure is a complete binary tree that satisfies the heap property, where any given node is either:
    * always greater than its child node/s and the key of the root node is the largest among all other nodes.
    This property is also called max heap property.

    * always smaller than the child node/s and the key of the root node is the smallest among all other nodes.
    This property is also called min heap property.

Heaps are usually used to implement priority queues, where the smallest (or largest) element is always at the root
of the tree. Heaps are also used in Heap Sort Algorithm.

A heap is typically represented as an array:
    * The root element will be at Arr[0].
    * For any ith node Arr[i]:
        * left child is stored at index 2i+1
        * Right child is stored at index 2i+2
        * Parent is stored at index floor((i-1)/2)

The Internal Implementation of the Max-Heap require 3 major steps:
    * Insertion: To insert a new element into the heap, it is added to the end of the array and then “bubbled up”
    until it satisfies the heap property.

    * Deletion: To delete the maximum element (the root of the heap), the last element in the array is swapped with
    the root, and the new root is “bubbled down” until it satisfies the heap property.

    * Heapify: A heapify operation can be used to create a max heap from an unsorted array.
        1. Start from the first index of non-leaf node whose index is given by "n/2 - 1"
        2. Set current element i as "largest".
        3. The index of left child is given by "2i + 1" and the right child is given by "2i + 2".
            * If "leftChild" is greater than "currentElement" (i.e. element at ith index), set "leftChildIndex" as "largest".
            * If "rightChild" is greater than element in "largest", set "rightChildIndex" as "largest".
        4. Swap "largest" with "currentElement"
        6. Repeat until the subtrees are also heapified.

    The time complexity of heapify in a max heap is O(n).

==========
Heap Sort
==========
Heap sort is a comparison-based sorting technique based on Binary Heap Data Structure.

It can be seen as an optimization over selection sort where we first find the max (or min) element and swap it with
the last (or first). We repeat the same process for the remaining elements. In Heap Sort, we use Binary Heap so that
we can quickly find and move the max element in O(Log n) instead of O(n) and hence achieve the O(n Log n) time complexity.

* Rearrange array elements so that they form a Max Heap.
* Repeat the following steps until the heap contains only one element:
    * Swap the root element of the heap (which is the largest element in current heap) with the last element of the heap.
    * Remove the last element of the heap (which is now in the correct position). We mainly reduce heap size and do
    not remove element from the actual array.
    * Heapify the remaining elements of the heap.

A good explanation can be found in this YouTube Tutorial: https://www.youtube.com/watch?v=1Rn10hHmp5I

Worst/Average/Best Time Complexity: O(n * log n)
Space Complexity:   O(log n), due to the recursive call stack. However, auxiliary space can be O(1) for iterative
                    implementation.

[14, 46, 43, 27, 57, 41, 45, 21, 70]

Ascending order:    [14, 21, 27, 41, 43, 45, 46, 57, 70]
Descending order:   [70, 57, 46, 45, 43, 41, 27, 21, 14]

"""


def heapify(lst: list[...], n: int, idx: int, reverse: bool) -> None:
    """
    Build Max/Min heap in a binary tree of size n at the subtree whose root's index is idx
    :param lst: the list to be sorted (can be seen as a binary tree in the sense of how Heap Sort works)
    :param n: the size of the list
    :param idx: the index of the subtree's root
    :param reverse: False => Max Heap, True => Min Heap
    :return: None
    """
    target = idx             # initially the target (max/min) value is in the root of the subtree
    left = idx * 2 + 1       # index of the left child
    right = idx * 2 + 2      # index of the right child

    # check whether: the left element index within the binary tree bounds + the left child hold the target value
    if left < n and [lst[left] > lst[target], lst[left] < lst[target]][reverse]:
        target = left

    # check whether: the right element index within the binary tree bounds + the right child hold the target value
    if right < n and [lst[right] > lst[target], lst[right] < lst[target]][reverse]:
        target = right

    # if the value of target has been changed => perform swap between the root and the child with the target value
    if target != idx:
        lst[idx], lst[target] = lst[target], lst[idx]

        # However, after the swap, the child value was replaced with value that is less (asc) than its previous value,
        # hence, the heap property might get broken in the child's subtree => perform heapify on the child subtree
        heapify(lst, n, target, reverse)


def heap_sort(lst: list[...], reverse: bool = False) -> None:
    """Heap sort implementation"""
    # Build the Max/Min heap by applying heapify to all non-leaf nodes.
    for i in range(len(lst) // 2 - 1, -1, -1):
        heapify(lst, len(lst), i, reverse)

    # Heap sort
    for i in range(len(lst) - 1, 0, -1):
        # replace the root (has the target value, i.e., maximum in Max Heap and minimum in Min Heap) with the ith element
        lst[0], lst[i] = lst[i], lst[0]

        # Apply heapify on the root to maintain the heap property
        # Note: by now, the ith element holds the ith largest_asc/smallest_desc element
        # => heapify should be executed on a reduced list [0, i[
        heapify(lst, i, 0, reverse)


def main():
    lst = [14, 46, 43, 27, 57, 41, 45, 21, 70]
    lst1 = lst[:]  # shallow copy

    heap_sort(lst, False)
    print(lst)

    heap_sort(lst1, True)
    print(lst1)


if __name__ == "__main__":
    main()
