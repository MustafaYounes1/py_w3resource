"""

Write a Python program to build a list, using an iterator function and an initial seed value.

In Python, we can create a list using a variety of methods. One such method is by using an iterator function and
an initial seed value.

Your task is to implement the unfold function that takes an iterator function and an initial seed value as arguments.
The iterator function accepts one argument (seed) and must always return a list with two elements ([value, nextSeed])
or False to terminate. The unfold function should use a generator function, fn_generator, that uses a while loop to
call the iterator function and yield the value until it returns False. Finally, the unfold function should use a
list comprehension to return the list that is produced by the generator, using the iterator function.

"""


def un_fold(fn, seed):
    """
    :param fn: the iterator function; accepts one argument (seed) and return a list of two elements [value, next_seed]
                or false to terminate
    :param seed: the initial seed value
    :return: a list produced by the generator function the uses the iterator function
    """

    def fn_generator(val):
        """
        Uses a while loop to call the iterator function and yield the value until it returns False
        :param val [value, next_seed] produced by the iterator function
        :return: the next value
        """
        while True:
            val = fn(val[1])
            if not val:
                break
            yield val[0]

    return [i for i in fn_generator([None, seed])]


def main():
    f = lambda n: False if n > 50 else [-n, n + 10]
    print(un_fold(f, 10))


if __name__ == "__main__":
    main()
