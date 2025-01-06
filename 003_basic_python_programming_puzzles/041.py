"""

Write a Python program to sort numbers based on strings.

Input: six one four two three
Output:
one two three four six

Input: six one four three two nine eight
Output:
one two three four six eight nine

Input: nine eight seven six five four three two one
Output:
one two three four five six seven eight nine

"""

__mapping = {
    k: v for k,v in zip(
        ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"],
        list(range(0, 10))
    )
}


def main():
    s = input("Enter a string of written numbers between zero and nine: ")
    print(" ".join(sorted(s.split(), key=lambda x: __mapping[x])))


if __name__ == "__main__":
    main()
