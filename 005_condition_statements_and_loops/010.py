"""

Write a Python program that iterates the integers from 0 to 50.
For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz".
For numbers that are multiples of three and five, print "FizzBuzz".
Sample Output :
fizzbuzz
1
2
fizz
4
buzz

"""


def main():
    for _ in range(0, 51):
        mul_3 = (_ % 3 == 0)
        mul_5 = (_ % 5 == 0)

        if mul_3 and mul_5:
            print('fizzbuzz')

        elif mul_3:
            print('fizz')

        elif mul_5:
            print('buzz')

        else:
            print(_)


if __name__ == "__main__":
    main()
