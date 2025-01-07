"""

Write a Python program to sort dict by value in descending order.

{'Math':81, 'Physics':83, 'Chemistry':87}

[('Chemistry', 87), ('Physics', 83), ('Math', 81)]

"""

from operator import itemgetter


def main():
    data = {'Math': 81, 'Physics': 83, 'Chemistry': 87}
    print(sorted(data.items(), key=itemgetter(1), reverse=True))


if __name__ == "__main__":
    main()
