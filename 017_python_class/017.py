"""

Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a
specific target number. Note: There will be one solution for each input and use the last index if an element was
duplicated.

[10, 20, 10, 40, 50, 60, 70], 50   =>    (3, 4)

"""


class Solver:
    @classmethod
    def solve(cls, lst: list, target: int) -> tuple:
        val_to_idx, out = {}, tuple()

        for idx, _ in enumerate(lst):
            if target - _ in val_to_idx:
                out = val_to_idx[target - _] + 1, idx + 1
                break
            else:
                val_to_idx[_] = idx

        return out


def main():
    lst, target = [10, 20, 10, 40, 50, 60, 70], 50
    print(Solver.solve(lst, target))


if __name__ == "__main__":
    main()
