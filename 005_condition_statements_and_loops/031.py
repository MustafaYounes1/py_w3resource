"""

Write a Python program to calculate a dog's age in dog years.
Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
Expected Output:

Input a dog's age in dog years: 15
The dog's age in human years is 73

"""


def main():
    n = int(input("Enter the dog year in dog years: "))

    if n <= 2:
        age = n * 10.5
    else:
        tmp = n - 2
        age = 21 + tmp * 4

    print(age)



if __name__ == "__main__":
    main()
