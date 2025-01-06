"""

Write a Python program to print the alphabet pattern 'E'.
Expected Output:

 *****
 *
 *
 ****
 *
 *
 *****

"""


def main():
    for i  in range(7):
        for j in range(5):

            if i in (0, 6):
                print('*', end="")

            elif i == 3:
                if j in range(4):
                    print("*", end="")

            else:
                print('*', end="")
                break

        print()

if __name__ == "__main__":
    main()
