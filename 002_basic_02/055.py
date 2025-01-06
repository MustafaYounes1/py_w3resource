"""

There are four different points on a plane, P(xp,yp), Q(xq, yq), R(xr, yr) and S(xs, ys).
Write a Python program to determine whether AB and CD are orthogonal.

Input:
xp,yp, xq, yq, xr, yr, xs and ys are -100 to 100 respectively and each value can be up to 5 digits after the decimal
point It is given as a real number including the number of. Output:

Output AB and CD are not orthogonal! or AB and CD are orthogonal!.

Input xp, yp, xq, yq, xr, yr, xs, ys:   4.5 -2.5 -2.5 4.5 3.5 3.5 3.8 -3.5
                                        AB and CD are not orthogonal!

Both lines have infinite slope then answer is no.
One line has infinite slope and if other line has 0 slope then answer is yes otherwise no.
Both lines have finite slope and their product is -1 then the answer is yes.

"""


def main():
    xp, yp, xq, yq, xr, yr, xs, ys = [
        float(_) for _ in input("Enter the 4 points x and y coordinates (space-separated): ").split()
    ]

    if (xq - xp) != 0:
        s1 = (yq - yp) / (xq - xp)
    else:
        s1 = None

    if (xs - xr) != 0:
        s2 = (ys - yr) / (xs - xr)
    else:
        s2 = None

    if s1 is None and s2 is None:
        print(False)

    elif s1 is None and s2 == 0:
        print(True)

    elif s1 == 0 and s2 is None:
        print(True)

    else:
        print(s1 * s2 == -1)


if __name__ == "__main__":
    main()
