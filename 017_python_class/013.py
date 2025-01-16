"""

Write a Python class to convert an integer to a Roman numeral.
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

1       =>  I
3       =>  III
8       =>  VIII
9       =>  IX
3549    =>  MMMDXLIX
4000    =>  MMMM

"""


class IntToRomanSolver:
    __ints = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    __romans = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']

    @classmethod
    def solve(cls, n: int) -> str:
        out_roman, idx = "", -1

        while n:
            div = n // cls.__ints[idx]
            n %= cls.__ints[idx]

            for _ in range(div):
                out_roman += cls.__romans[idx]

            idx -= 1

        return out_roman


def main():
    nums = (1, 3, 8, 9, 3549, 4000)
    for n in nums:
        print(IntToRomanSolver.solve(n))


if __name__ == "__main__":
    main()
