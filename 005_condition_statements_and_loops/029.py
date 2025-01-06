"""

Write a Python program to print the alphabet pattern 'X'.
Expected Output:

 *   *
 *   *
  * *
   *
  * *
 *   *
 *   *

"""


def main():
    for i in range(7):
        for j in range(5):

            if (i in (0, 1, 5, 6) and j in (0, 4)) or (i in (2, 4) and j in (1, 3)) or (i == 3 and j == 2):
                print('*', end='')
            else:
                print(' ', end='')

        print()


if __name__ == "__main__":
    main()
