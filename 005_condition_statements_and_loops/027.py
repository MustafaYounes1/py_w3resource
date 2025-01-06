"""

Write a Python program to print the alphabet pattern 'T'.
Expected Output:
 *****
   *
   *
   *
   *
   *
   *

"""


def main():
    for i in range(7):
        for j in range(5):

            if i == 0 or j == 2:
                print('*', end='')
            else:
                print(' ', end='')

        print()


if __name__ == "__main__":
    main()
