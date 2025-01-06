"""

Remove duplicates from a list while preserving order.

e.g.    lst = [1, 2, 2, 3, 4, 4, 5]     =>  [1, 2, 3, 4, 5]
"""


def main():
    lst = [1, 2, 2, 3, 4, 4, 5]
    seen = set()
    out = []

    for _ in lst:
        if _ not in seen:
            out.append(_)
            seen.add(_)

    print(out)

if __name__ == "__main__":
    main()
