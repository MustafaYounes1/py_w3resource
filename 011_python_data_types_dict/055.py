"""

Write a Python program to access dictionary key's element by index.

d = {'physics': 80, 'math': 90, 'chemistry': 86}

physics
math
chemistry

"""


def main():
    d = {'physics': 80, 'math': 90, 'chemistry': 86}
    keys = list(d.keys())
    for idx in range(len(d)):
        print(keys[idx])


if __name__ == "__main__":
    main()
