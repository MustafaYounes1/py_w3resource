"""

Write a Python program to print the alphabet pattern 'R'.
Expected Output:

 ****
 *   *
 *   *
 ****
 * *
 *  *
 *   *

"""


def main():
    for i in range(7):
        for j in range(5):

            if (j == 0) or (i in (0, 3) and j < 4) or (j == 4 and i in (1, 2))  or (j == (i-2)):
                print('*', end='')
            else:
                print(' ', end='')

        print()


if __name__ == "__main__":
    main()
