"""

Write a Python program to create a class representing a queue data structure. Include methods to:
    1. enqueue and dequeue elements from the queue.
    2. return the size of the queue
    3. check whether an element exists in the queue
    3. get a list of the queue

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

queue.to_list()         =>  [10, 20, 30, 40, 50]

queue.dequeue()         =>  10
queue.dequeue()         =>  20
queue.dequeue()         =>  30

len(queue)              =>  2

20 in queue             =>  False

queue.to_list()         =>  [40, 50]

"""


class Queue:
    def __init__(self):
        self.__data: list[object] = []

    def enqueue(self, item: object) -> None:
        """Add an item to the queue"""
        self.__data.append(item)

    def dequeue(self) -> object:
        """Pop the first element (FIFO), would raise an IndexError if the queue is empty"""
        if not self.__data:
            raise IndexError("Queue is empty")

        return self.__data.pop(0)

    def __contains__(self, item: object) -> bool:
        """Check if an item exists in the queue"""
        return item in self.__data

    def __len__(self) -> int:
        """Return teh size of the queue"""
        return len(self.__data)

    def to_list(self) -> list[object]:
        """Return the objects of the queue as a list"""
        return self.__data


def main():
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.enqueue(50)
    print(queue.to_list())

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(len(queue))
    print(20 in queue)
    print(queue.to_list())


if __name__ == "__main__":
    main()
