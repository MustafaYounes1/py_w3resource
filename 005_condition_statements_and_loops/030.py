"""

Write a Python program to print the alphabet pattern 'Z'.
Expected Output:

*******
     *
    *
   *
  *
 *
*******

"""


def main():
    for i in range(7):
        for j in range(7):

            if i in (0, 6) or (j == 6 - i):
                print('*', end='')
            else:
                print(' ', end='')

        print()

if __name__ == "__main__":
    main()
