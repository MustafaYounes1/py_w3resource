"""

Write a Python program to find the index of the matching parentheses for each character in a given string.

Input: ()(())   =>  [1, 0, 5, 4, 3, 2]
Input: ()()()   =>  [1, 0, 3, 2, 5, 4]
Input: ((()))   =>  [5, 4, 3, 2, 1, 0]

"""

__data = [
    "()(())",
    "()()()",
    "((()))"
]


def match(s):
    # Convert the string of parentheses into a list
    a = list(s)
    # Initialize an empty stack to keep track of the indices of opening parentheses
    stack = []

    # Iterate through the enumerated characters in the list 'a'
    for i, c in enumerate(a):
        # Check if the character is an opening parenthesis "("
        if c == "(":
            # Push the current index onto the stack
            stack.append(i)
        else:
            # Update the indices of the matching parentheses
            a[stack[-1]] = i
            a[i] = stack.pop()

    # Return the list with indices of the matching parentheses
    return a


def main():
    for s in __data:
        print(match(s))


if __name__ == "__main__":
    main()
