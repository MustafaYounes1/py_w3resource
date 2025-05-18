"""

Write a Python program that adds integer numbers from the data stream to a heapq and computes the median of all
elements. Use the heap queue algorithm.

Median, by definition, is the middle value in an ordered list of numbers. If the list has an odd number of elements,
the median is simply the middle element. If the list has an even number of elements, there is no single middle element,
so the median is calculated by taking the average of the two middle numbers.

=========
Approach
=========
To find the median efficiently, we need a data structure that allows quick access to the middle elements. Utilizing two
heaps is an elegant solution: a max heap to store the smaller half of the numbers and a min heap to store the larger
half. This way, the largest number in the smaller half or the smallest number in the larger half can easily give us the
median.

By balancing the heaps so that their size differs by at most one, we ensure that we either have a single middle element
when the combined size is odd (this will be at the top of the max heap), or two middle elements when the combined
size is even (the top of each heap).

Task: given a list of integers, find the median after adding each item from the list

[5, 15, 1, 3, 2, 8]     ->  [5, 10.0, 5, 4.0, 3, 4.0]
[2, 2, 2, 2]            ->  [2, 2.0, 2, 2.0]
[1, 2, 3, 4, 5]         ->  [1, 1.5, 2, 2.5, 3]

"""

from heapq import heappush, heappop


class MedianFinder:
    """A class to efficiently find the median from a stream of values added during runtime"""
    def __init__(self):
        # the left half the has the smaller values (max-heap, because we want to get the largest item in this half)
        self.__left_half: list[int | float] = []

        # the right half the has the larger values (min-heap, because we want to get the smallest item in this half)
        self.__right_half: list[int | float] = []

    def add_value(self, val: int | float) -> None:
        """Add a value"""
        # add the new value to the left half (half of smaller values) (max-heap -> -val)
        heappush(self.__left_half, -val)

        # maintain order: move the largest number from the left half to the right half (min-heap -> positive)
        heappush(self.__right_half, -heappop(self.__left_half))

        # balance the two halves
        # at the end, their sizes would either be the same or differ by at most 1 (left half would have one more item)
        if len(self.__right_half) > len(self.__left_half):
            heappush(self.__left_half, -heappop(self.__right_half))

    @property
    def median(self) -> int | float:
        """Find the median efficiently by only accessing the root of both heaps"""

        # If the heaps have equal size, the median is the average of the two heap's top elements
        if len(self.__left_half) == len(self.__right_half):
            return (-self.__left_half[0] + self.__right_half[0]) / 2

        # Otherwise, return the top element of the left heap
        else:
            return -self.__left_half[0]


def main():
    data = [
        [5, 15, 1, 3, 2, 8],
        [2, 2, 2, 2],
        [1, 2, 3, 4, 5]
    ]

    for lst in data:
        res, solver = [], MedianFinder()

        for _ in lst:
            solver.add_value(_)
            res.append(solver.median)

        print(res)


if __name__ == "__main__":
    main()
