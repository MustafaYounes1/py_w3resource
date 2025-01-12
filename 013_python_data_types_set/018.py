"""

Write a Python program to check if a given set is a superset of a given set

num1 =  {1, 2, 3, 4, 5, 7}
num2 =  {2, 4}
num3 =  {2, 4}

mum1 is superset of num2    =>  True
mum2 is superset of num3    =>  False
mum3 is superset of num2    =>  False

"""


def main():
    num1 = {1, 2, 3, 4, 5, 7}
    num2 = {2, 4}
    num3 = {2, 4}

    # Note 'issuperset()' == '>='
    print(num1 > num2)
    print(num2 > num3)
    print(num3 > num2)


if __name__ == "__main__":
    main()
