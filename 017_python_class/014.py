"""

Write a Python class to convert a Roman numeral to an integer.
Note: Below table shows the list of Roman symbols including their corresponding integer values also:

Symbols	    Values
I	        1
IV  	    4
V	        5
IX	        9
X	        10
XL	        40
L	        50
XC	        90
C	        100
CD	        400
D	        500
CM	        900
M	        1000

I           =>  1
III         =>  3
VIII        =>  8
IX          =>  9
C           =>  100
MMMDXLIX    =>  3549
MMMCMLXXXVI =>  3986
MMMM        =>  4000

"""


class RomanToIntSolver:
    __ints = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    __romans = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']

    @classmethod
    def solve(cls, r: str) -> int:
        out_int, idx = 0, -1

        while r:
            if r.startswith(cls.__romans[idx]):
                out_int += cls.__ints[idx]
                r = r.replace(cls.__romans[idx], "", 1)
            else:
                idx -= 1

        return out_int


def main():
    romans = ("I", "III", "VIII", "IX", "C", "MMMDXLIX", "MMMCMLXXXVI", "MMMM")
    for r in romans:
        print(RomanToIntSolver.solve(r))


if __name__ == "__main__":
    main()
