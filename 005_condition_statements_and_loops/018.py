"""

Write a Python program to print the alphabet pattern 'D'.
Expected Output:

 ****
 *   *
 *   *
 *   *
 *   *
 *   *
 ****

"""


def main():
    for i in range(7):
        for j in range(5):

            if i in (0, 6):
                if j in range(4):
                    print('*', end="")
                else:
                    print(' ', end="")

            else:
                if j in (0, 4):
                    print('*', end="")
                else:
                    print(' ', end="")

        print()


if __name__ == "__main__":
    main()
