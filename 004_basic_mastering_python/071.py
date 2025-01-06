"""

Find the longest common prefix among a list of strings.

lst = ["flower", "flow", "flight"]      =>  fl

"""


def main():
    lst = ["flower", "flow", "flight"]
    out = ""

    for ps in zip(*lst):
        if len(set(ps)) == 1:
            out += ps[0]
        else:
            break

    print(out)


if __name__ == "__main__":
    main()
