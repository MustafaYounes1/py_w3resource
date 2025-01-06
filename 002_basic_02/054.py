"""

If you draw a straight line on a plane, the plane is divided into two regions. For example, if you draw two straight
lines in parallel, you get three areas, and if you draw vertically one to the other you get 4 areas.

Write a Python program to create the maximum number of regions obtained by drawing n given non-parallel straight lines.
Input:
(1 <= n <= 10,000)
Input number of straight lines (o to exit):     5
Number of regions:                              16

One line can divide a plane into two regions, two non-parallel lines can divide a plane into 4 regions and three
non-parallel lines can divide into 7 regions, and so on

L(2) – L(1) = 2 … (i)
L(3) – L(2) = 3 … (ii)
L(4) – L(3) = 4 … (iii)
. . .
. . .
L(n) – L(n-1) = n ; … (n)

Adding all the above equation we get,
L(n) – L(1) = 2 + 3 + 4 + 5 + 6 + 7 + …… + n ;
L(n) = L(1) + 2 + 3 + 4 + 5 + 6 + 7 + …… + n ;
L(n) = 2 + 2 + 3 + 4 + 5 + 6 + 7 + …… + n ;
L(n) = 1 + 2 + 3 + 4 + 5 + 6 + 7 + …… + n + 1 ;

L(n) = 1 + 2 + 3 + 4 + 5 + 6 + 7 + …… + n
sum of the first n elements in an AP: n/2 [2a + (n-1)d] => 1/2 (n^2 + n)

there was a "+1" left => L(n) = (n^2 + n) / 2 + 1

"""


def main():
    n = int(input("Enter the number of non-parallel lines: "))
    n_regions = int((pow(n, 2) + n) / 2 + 1)
    print(n_regions)


if __name__ == "__main__":
    main()
