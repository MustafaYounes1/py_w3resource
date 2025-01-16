"""

Write a Python program that creates a float array out of the bytes representation of another float array

a1:     [1.1, 2.2, 3.3]
a2  =>  [1.100000023841858, 2.200000047683716, 3.299999952316284]

"""

from array import array


def main():
    a1 = array('f', [1.1, 2.2, 3.3])

    a2 = array('f')
    a2.frombytes(a1.tobytes())

    print(a2.tolist())

if __name__ == "__main__":
    main()
