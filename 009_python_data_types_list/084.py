"""

Write a Python program to round the numbers in a given list, print the minimum and maximum numbers and multiply the
numbers by 5. Print the unique numbers in ascending order separated by space.

[22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]

Minimum value: 4
Maximum value: 22
20 25 45 55 60 70 80 90 110

"""


def main():
    lst = [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
    lst = list(map(round, lst))
    print(f"Minimum value: {min(lst)}")
    print(f"Maximum value: {max(lst)}")
    print(" ".join(list(map(lambda _: str(_ * 5), sorted(set(lst))))))


if __name__ == "__main__":
    main()
