"""

Write a Python program to print the alphabet pattern 'M'.
Expected Output:

  *       *
  *       *
  * *   * *
  *   *   *
  *       *
  *       *
  *       *

"""


def main():
    for i in range(7):
        for j in range(5):

            if i == 2:
                if j != 2:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')

            elif i == 3:
                if j in (0, 2, 4):
                    print('*', end=' ')
                else:
                    print(' ', end=' ')

            else:
                if j in (0, 4):
                    print('*', end=' ')
                else:
                    print(' ', end=' ')

        print()


if __name__ == "__main__":
    main()
