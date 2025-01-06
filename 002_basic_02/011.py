"""

Write a Python program to check the sum of three elements (each from an array) from three arrays is equal to a
target value. Print all those three-element combinations.

Sample data:
    X = [10, 20, 20, 20]
    Y = [10, 20, 30, 40]
    Z = [10, 30, 40, 20]
target = 70

"""

from functools import partial
from itertools import product, starmap


def main():
    x = [10, 20, 20, 20]
    y = [10, 20, 30, 40]
    z = [10, 30, 40, 20]
    target = 70

    def is_valid(tar, *t):
        if sum(t) == tar:
            return True, t
        else:
            return False, t

    # Return a new partial object which when called will behave like func called with the positional arguments args
    # and keyword arguments keywords. If more arguments are supplied to the call, they are appended to args.
    # If additional keyword arguments are supplied, they extend and override keywords.
    # partial objects are callable objects created by partial().
    func = partial(is_valid, target)

    target_comb = set()

    # 'starmap' Make an iterator that computes the function using arguments obtained from the iterable.
    # Used instead of map() when argument parameters have already been “pre-zipped” into tuples.
    # The difference between map() and starmap() parallels the distinction between function(a,b) and function(*c)

    # 'product' Cartesian product of the input iterables.
    # Roughly equivalent to nested for-loops in a generator expression. For example, product(A, B) returns the same
    # as ((x,y) for x in A for y in B).
    results = starmap(func, product(x, y, z))
    for res in results:
        if res[0]:
            target_comb.update([res[1]])

    print(target_comb)


if __name__ == "__main__":
    main()
