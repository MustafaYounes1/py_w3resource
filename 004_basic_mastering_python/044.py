"""

Create a list and set the values between the 25th and 75th percentile to 0.

lst = [10, 20, 30, 40, 50]

[10, 0, 0, 0, 50]

"""


def main():
    lst = [10, 20, 30, 40, 50]
    s_lst = sorted(lst)
    p_25 = s_lst[int(len(s_lst) * 0.25)]
    p_75 = s_lst[int(len(s_lst) * 0.75)]
    print([0 if p_25 <= _ <= p_75 else _ for _ in lst])


if __name__ == "__main__":
    main()
