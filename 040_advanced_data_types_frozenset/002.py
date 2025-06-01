"""

Write a Python program that converts a "frozen set" to a regular set and vice versa. Compare the differences between
these two data types.


"""
import builtins


def compare_types(t1: builtins.type, t2: builtins.type) -> tuple[set, set, set]:
    """Compare the attributes of two types and return a tuple of 3 sets: common, only in t1, only in t2"""
    t1_attr = {_ for _ in dir(t1) if not _.startswith("_")}
    t2_attr = {_ for _ in dir(t2) if not _.startswith("_")}
    return t1_attr & t2_attr, t1_attr - t2_attr, t2_attr - t1_attr


def main():
    data = [1, 2]

    s = set(data)  # create a set from an iterable
    fs = frozenset(s)  # create a frozenset from a set
    s = set(fs)  # create a set from a frozen set
    print(s, fs)

    s_fs_attr, s_attr, fs_attr = compare_types(set, frozenset)
    print(f"Common in sets and frozen sets: {s_fs_attr}")
    print(f"Only in set:                    {s_attr}")
    print(f"Only in frozenset:              {fs_attr}")


if __name__ == "__main__":
    main()
