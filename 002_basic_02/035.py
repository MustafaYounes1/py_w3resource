"""

Write a Python program which solve the equation:
    ax+by=c
    dx+ey=f
Print the values of x, y where a, b, c, d, e and f are given.

a,b,c,d,e,f separated by a single space.
(-1,000 <= a,b,c,d,e,f <= 1,000)

D   =   a   b   = ae - db
        d   e

Dx  =   c   b   = ce - bf
        f   e

Dy  =   a   c   = af - cd
        d   f

x = Dx / D
y = Dy / D

Input the value of a, b, c, d, e, f:    5 8 6 7 9 4
Values of x and y:                      -2.000 2.000

"""


def main():
    a, b, c, d, e, f = [int(_) for _ in input("Enter the 6 coefficients space-separated: ").split()]
    det = a * e - d * b
    x = (c * e - b * f) / det
    y = (a * f - c * d) / det
    print(f"x = {x:.3f}, y = {y:.3f}")


if __name__ == "__main__":
    main()
