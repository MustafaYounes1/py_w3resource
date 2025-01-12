"""

Write a python program to create a dict which has the following key-value pair:

(k: v); where k is a set of two values: ("Red", "Green") and the v is "success"

try to access the key above in the dictionary   =>  success

"""


def main():
    k, v = frozenset(["Red", "Green"]), "success"
    d = {k: v}
    print(d[k])


if __name__ == "__main__":
    main()
