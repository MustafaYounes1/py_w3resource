"""

Write a Python program to count Uppercase, Lowercase, special characters and numeric values in a given string.

@W3Resource.Com

#upper     : 3
#lower     : 9
#puctuation: 2
#digits    : 1

"""

from string import ascii_lowercase, ascii_uppercase, punctuation, digits


def main():
    s = input("Enter a string: ")
    ls, us, ps, ds = [], [], [], []

    for _ in s:
        if _ in ascii_uppercase:
            us.append(_)

        elif _ in ascii_lowercase:
            ls.append(_)

        elif _ in punctuation:
            ps.append(_)

        elif _ in digits:
            ds.append(_)

        else:
            pass

    print(f"#upper     : {len(us)}")
    print(f"#lower     : {len(ls)}")
    print(f"#puctuation: {len(ps)}")
    print(f"#digits    : {len(ds)}")


if __name__ == "__main__":
    main()
