"""

Write a Python program to create a class representing a stack data structure. Include methods for:
    pushing
    popping
    check if the stack is empty
    the len of the stack
    peek at the last element if there are any elements without removing it

stack.push(0)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

Stack size:     5
Last element:   4

// pop an element from the stack //
Stack size:     4
Last element:   3

"""

from typing import List


class Stack:
    """Simple stack implementation"""
    def __init__(self):
        self.__s: List[object] = []

    def __len__(self) -> int:
        """The size of the stack"""
        return len(self.__s)

    @property
    def is_empty(self) -> bool:
        """Check whether the stack is empty"""
        return len(self) == 0

    def push(self, item: object) -> None:
        """Push an item to the stack"""
        self.__s.append(item)

    def pop(self) -> object:
        """Pop an item from the stack"""
        if self.is_empty:
            raise IndexError("The stack is empty")

        return self.__s.pop()

    def peek(self) -> object:
        """Peek at the last element of the stack"""
        if self.is_empty:
            raise IndexError("The stack is empty")
        else:
            return self.__s[-1]


def main():
    stack = Stack()

    stack.push(0)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(f"Stack size:     {len(stack)}")
    print(f"Last element:   {stack.peek()}")

    stack.pop()
    print(f"Stack size:     {len(stack)}")
    print(f"Last element:   {stack.peek()}")


if __name__ == "__main__":
    main()
