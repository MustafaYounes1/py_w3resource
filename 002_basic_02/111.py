"""

Write a Python program which checks whether two circles in the same plane (with the same center (x,y) and radius)
intersect. If intersection occurs, return true, otherwise return false.

Sample Input: (center_x, center_y, radius)
([1,2, 4], [1,2, 8])        =>  True
([0,0, 2], [10,10, 5])      =>  False

"""

from math import sqrt


def main():
    c1_x, c1_y, r1 = list(map(float, input("Enter the first circle: (x, y, r) ").split()))
    c2_x, c2_y, r2 = list(map(float, input("Enter the second circle: (x, y, r) ").split()))

    dis = sqrt(pow(c1_x - c2_x, 2) + pow(c2_x - c2_x, 2))

    print(dis <= (r1 + r2))


if __name__ == "__main__":
    main()
