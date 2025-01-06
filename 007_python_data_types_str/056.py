"""

Write a Python program to find the second most repeated word in a given string.

Both of these issues are fixed by postponing the evaluation of annotations. Instead of compiling code which executes
expressions in annotations at their definition time, the compiler stores the annotation in a string form equivalent to
the AST of the expression in question. If needed, annotations can be resolved at runtime using typing.get_type_hints().
In the common case where this is not required, the annotations are cheaper to store (since short strings are interned
by the interpreter) and make startup time faster.


"""

from itertools import groupby
from string import punctuation


def main():
    s = """Both of these issues are fixed by postponing the evaluation of annotations. Instead of compiling code 
    which executes expressions in annotations at their definition time, the compiler stores the annotation in a 
    string form equivalent to the AST of the expression in question. If needed, annotations can be resolved at 
    runtime using typing.get_type_hints(). In the common case where this is not required, the annotations are cheaper 
    to store (since short strings are interned by the interpreter) and make startup time faster."""

    # all to lowercase and clean the punctuation
    s = s.lower().translate(str.maketrans("", "", punctuation)).split()

    # sorted according the appearance counts so the itertools groupby can work properly
    words = sorted(set(filter(lambda _: s.count(_) > 1, s)), reverse=True, key=lambda _: s.count(_))

    # Because the source is shared, when the groupby() object is advanced, the previous group is no longer visible.
    counts, groups = [], []

    for k, v in groupby(words, lambda _: s.count(_)):
        counts.append(k)
        groups.append(list(v))

    print(f"Second most repeated word(s): {groups[1] if len(groups) > 1 else None}")
    print(f"the length of the second most repeated word(s): {counts[1] if len(counts) > 1 else None}")


if __name__ == "__main__":
    main()
