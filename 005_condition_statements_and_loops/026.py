"""

Write a Python program to print the following patterns.
Expected Output:

  ****
 *
 *
  ***
     *
     *
 ****

 ooooooooooooooooo
ooooooooooooooooo
ooooooooooooooooo
oooo
oooo
oooo
ooooooooooooooooo
ooooooooooooooooo
ooooooooooooooooo
             oooo
             oooo
             oooo
ooooooooooooooooo
ooooooooooooooooo
ooooooooooooooooo

"""


def main():
    for i in range(7):
        for j in range(5):

            if (j == 0 and i in (1, 2, 6)) or (1 <= j <= 3 and i in (0, 3, 6)) or (j == 4 and i in (0, 4, 5)):
                print('*', end='')
            else:
                print(' ', end='')

        print()

    print()

    for i in range(15):
        for j in range(17):

            if (i == 0 and 1 <= j <= 16) or (i in (1, 2, 6, 7, 8, 12, 13, 14) and 0 <= j < 16) or (
                    i in (3, 4, 5) and 0 <= j <= 3) or (i in (9, 10, 11) and 13 <= j < 16):
                print('o', end='')
            else:
                print(' ', end='')

        print()


if __name__ == "__main__":
    main()
