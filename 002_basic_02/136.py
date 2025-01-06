"""

Write a Python program to reverse all words of odd lengths.

Original string: The quick brown fox jumps over the lazy dog    =>  ehT kciuq nworb xof spmuj over eht lazy god
Original string: Python Exercises                               =>  Python sesicrexE

"""


def main():
    seq = input("Enter a string: ")
    out_str = ' '.join(i[::-1] if len(i) % 2 else i for i in seq.split())
    print(out_str)


if __name__ == "__main__":
    main()
