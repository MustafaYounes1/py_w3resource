"""

Write a Python program to print the length of the series and the series from the given 3rd term, 3rd last term and
the sum of an arithmetic progression series.

In AP, we will come across some main terms, which are denoted as:
    First term (a)
    Common difference (d)
    nth Term (an)
    Sum of the first n terms (Sn)

a, a + d, a + 2d, a + 3d, a + 4d, ………. ,a + (n – 1) d

d = a2 – a1 = a3 – a2 = ……. = an – an – 1

nth Term of an AP = an = a + (n − 1) × d

sum of the first n terms: Sn = n/2[2a + (n − 1) × d]

Sum of AP when the Last Term is Given: S  = n/2 (first term + last term)

Solution:
---------
Third term =        a + 2d = k1, say (k1 is known)
Third last term =   a + (n-3)d = k2 (k2 is known)
Sum of the AP =     n/2 [2a + (n-1)d]
Alright, so now we have the equations. Let's add the first two equations.
2a + (n-1)d = k1 + k2
Putting this in the formula for sum of terms, S = n/2(k1+k2).
Hence, n = 2S/(k1+k2)
Now subtract the first equation from the second.
(n-5)d = k2 - k1. Since you know n, you can find d.
And now since you know the value of d, substitute it in the first equation to find a, the first term.

Sample Data:
    Input third term of the series: 3
    Input 3rd last term: 3
    Input Sum of the series: 15

Length of the series: 5
Series: 1 2 3 4 5

Sample Data:
    Input third term of the series: 3
    Input 3rd last term: 6
    Sum of the series: 36

Length of the series:  8
Series: 1 2 3 4 5 6 7 8

"""


def main():
    f_third = int(input("Enter the first third element of the AP: "))
    l_third = int(input("Enter the last third element of the AP: "))
    s = int(input("Enter sum of the AP: "))

    n = 2 * s // (f_third + l_third)

    if (n - 5) == 0:
        d = (s - 3 * f_third) // 6
    else:
        d = (l_third - f_third) // (n - 5)

    a = f_third - 2 * d

    for _ in range(1, int(n) + 1):
        print(a + (_ - 1) * d, end=" ")


if __name__ == "__main__":
    main()
