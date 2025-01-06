"""

Write a Python program to find the closest palindrome to a given string.

cat         =>  cac
madan       =>  madam
radivider   =>  radividar
madan       =>  madam
abc         =>  aba
racecbr     =>  racecar

"""

__data = [
    "cat",
    "madan",
    "radivider",
    "madan",
    "abc",
    "racecbr"
]


def main():
    for w in __data:
        c_idx = len(w) // 2
        out_str = w[:c_idx]

        for c in w[c_idx::-1]:
            out_str += c

        print(out_str)


if __name__ == "__main__":
    main()
