"""

Write a Python program to check whether two given lines are parallel or not.
Note: Parallel lines are two or more lines that never intersect. Parallel Lines are like railroad tracks that never intersect.
The General Form of the equation of a straight line is: ax + by = c
The said straight line is represented in a list as [a, b, c]
Example of two parallel lines:
x + 4y = 10 and x + 4y = 14

Sample Input:
([2,3,4], [2,3,8])      =>  True
([2,3,4], [4,-3,8])     =>  False

"""


def main():
    l1 = list(map(float, input("The formula of the first line: (a, b, c) ").split()))
    l2 = list(map(float, input("The formula of the second line: (a, b, c) ").split()))

    print(-l1[0] / l1[1] == -l2[0] / l2[1])


if __name__ == "__main__":
    main()
