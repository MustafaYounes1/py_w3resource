"""

Write a Python program to combine each line from first file with the corresponding line in second file.
    Input file 1: "013a.txt"
    Input file 2: "013b.txt"
    Output file: "013c.txt"

"013c.txt" would get created and would have the following content:

Python Programming Language
w3resource Exercises

"""

from itertools import zip_longest


__in_f1_path = "013a.txt"
__in_f2_path = "013b.txt"
__out_f_path = "013c.txt"


def main():
    with open(__out_f_path, "w") as f:
        f1 = open(__in_f1_path)
        f2 = open(__in_f2_path)

        for l1, l2 in zip_longest(f1, f2, fillvalue=""):
            f.write("%s %s\n" % (l1.strip('\n'), l2.strip('\n')))

        f1.close()
        f2.close()


if __name__ == "__main__":
    main()
