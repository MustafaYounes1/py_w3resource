"""

Write a Python program to encode a complex number to json data.

2 + 3j  =>  '[2.0, 3.0]'

"""
import json


def serialize_complex(c: complex):
    if isinstance(c, complex):
        return [c.real, c.imag]

    raise TypeError(repr(c) + " can't be serialized to json data!")


def main():
    c = 2 + 3j
    print(json.dumps(c, default=serialize_complex))


if __name__ == "__main__":
    main()
