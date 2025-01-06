"""

Write a Python function to insert a string in the middle of a string.

Sample function and result :
insert_sting_middle('[[]]', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}

"""


def insert_sting_middle(s1, s2):
    c = len(s1) // 2
    return s1[:c] + s2 + s1[c:]


def main():
    print(insert_sting_middle('[[]]', 'Python'))
    print(insert_sting_middle('{{}}', 'PHP'))


if __name__ == "__main__":
    main()
