"""

Write a Python program to determine the direction ('increasing' or 'decreasing') of monotonic sequence numbers.

Input:
[1, 2, 3, 4, 5, 6]
Output:
Increasing.

Input:
[6, 5, 4, 3, 2, 1]
Output:
Decreasing.

Input:
[19, 19, 5, 5, 5, 5, 5]
Output:
Not a monotonic sequence!

"""


def main():
    seq = list(map(int, input("Enter a list of comma-separated integers: ").split(", ")))

    state = ""
    for a, b in zip(seq, seq[1:]):
        if b > a and (not state or state == "Increasing"):
            state = "Increasing"

        elif a > b and (not state or state == "Decreasing"):
            state = "Decreasing"

        else:
            state = "Not a monotonic sequence!"
            break

    print(state)

if __name__ == "__main__":
    main()
