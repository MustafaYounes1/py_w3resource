"""

Write a Python script to sort (ascending and descending) a dictionary by value.

{1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

Ascending:   {0: 0, 1: 2, 2: 1, 3: 4, 4: 3}
Descending:  {4: 3, 3: 4, 2: 1, 1: 2, 0: 0}

"""


def main():
    d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    print("Ascending:   {}".format({k: d.get(k) for k in sorted(d)}))
    print("Descending:  {}".format({k: d.get(k) for k in sorted(d, reverse=True)}))


if __name__ == "__main__":
    main()
