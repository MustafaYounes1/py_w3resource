"""

Write a Python program to print the alphabet pattern 'P'.
Expected Output:

 ****
 *   *
 *   *
 ****
 *
 *
 *

"""


def main():
    for i in range(7):
        for j in range(5):

            if i in (0, 3):
                if j <= 3:
                    print('*', end='')
                else:
                    print(' ', end='')

            elif i in (1, 2):
                if j in (0, 4):
                    print('*', end='')
                else:
                    print(' ', end='')

            else:
                print('*', end='')
                break

        print()


if __name__ == "__main__":
    main()
