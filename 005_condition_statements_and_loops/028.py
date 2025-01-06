"""

Write a Python program to print the alphabet pattern 'U'.
Expected Output:

 *   *
 *   *
 *   *
 *   *
 *   *
 *   *
  ***

"""


def main():
    for i in range(7):
        for j in range(5):

            if (i != 6 and j in (0, 4)) or (i == 6 and 1 <= j <= 3):
                print('*', end='')
            else:
                print(' ', end='')

        print()


if __name__ == "__main__":
    main()
