"""

Write a Python program to split a given list into specified-sized chunks.

[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]

3   =>  [[12, 45, 23], [67, 78, 90], [45, 32, 100], [76, 38, 62], [73, 29, 83]]
4   =>  [[12, 45, 23, 67], [78, 90, 45, 32], [100, 76, 38, 62], [73, 29, 83]]
5   =>  [[12, 45, 23, 67, 78], [90, 45, 32, 100, 76], [38, 62, 73, 29, 83]]

"""


def main():
    lst = [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
    batches = [3, 4, 5]

    for bs in batches:
        print([lst[idx: idx + bs] for idx in range(0, len(lst), bs)])


if __name__ == "__main__":
    main()
