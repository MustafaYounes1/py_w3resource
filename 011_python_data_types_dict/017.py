"""

Write a Python program to remove duplicates from the dictionary.


student_data = {
    'id1': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']},
    'id2': {'name': ['David'], 'class': ['V'], 'subject_integration': ['english, math, science']},
    'id3': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']},
    'id4': {'name': ['Surya'], 'class': ['V'], 'subject_integration': ['english, math, science']}
}

Both id1 and id3 holds the same data, and just one needs to be keeped

{
    'id2': {'subject_integration': ['english, math, science'], 'class': ['V'], 'name': ['David']},
    'id4': {'subject_integration': ['english, math, science'], 'class': ['V'], 'name': ['Surya']},
    'id1': {'subject_integration': ['english, math, science'], 'class': ['V'], 'name': ['Sara']}
}
"""


def main():
    student_data = {
        'id1': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']},
        'id2': {'name': ['David'], 'class': ['V'], 'subject_integration': ['english, math, science']},
        'id3': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']},
        'id4': {'name': ['Surya'], 'class': ['V'], 'subject_integration': ['english, math, science']}
    }

    out = {}
    for k, v in student_data.items():
        if v not in out.values():
            out[k] = v

    print(out)

if __name__ == "__main__":
    main()
