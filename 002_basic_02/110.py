"""

Write a Python program to remove duplicate numbers (all the occurrences) from a given list of numbers.

Sample Input:
([1,2,3,2,3,4,5])   =>  [1, 4, 5]
([1,2,3,2,4,5])     =>  [1, 3, 4, 5]
([1,2,3,4,5])       =>  [1, 2, 3, 4, 5]

"""


def main():
    seq = list(map(int, input("Enter a list of space-separated integers: ").split()))
    print(
        [_ for _ in seq if seq.count(_) == 1]
    )


if __name__ == "__main__":
    main()
