"""

Write a Python program to create a deque with the elements: ['Red', 'Green', 'White']

1. Add 'Pink' to the left
2. Add 'Orange' to the right
3. Remove one element from the right
4. Remove one element from the left
5. Reverse the deque

['White', 'Green', 'Red']

"""

from collections import deque


def main():
    d = deque(['Red', 'Green', 'White'])

    d.appendleft('Pink')
    d.append('Orange')
    d.pop()
    d.popleft()
    d.reverse()

    print(list(d))


if __name__ == "__main__":
    main()
