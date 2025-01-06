"""

 Write a Python program to print the alphabet pattern 'L'.
Expected Output:

 *
 *
 *
 *
 *
 *
 *****

"""


def main():
    for i in range(7):
        for j in range(5):

            if i != 6:
                print('*', end='')
                break

            else:
                print('*', end='')

        print()


if __name__ == "__main__":
    main()
