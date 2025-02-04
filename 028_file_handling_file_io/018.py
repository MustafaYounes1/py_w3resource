"""

Write a Python program to extract content from various text files and puts them into a list.
    Input file 1: 001.txt
    Input file 2: 007.txt

[
    'Welcome to w3resource.com.', 'Append this text.Append this text.Append this text.', 'Append this text.',
    'Append this text.', 'Append this text.', 'Append this text.', 'What is Python language?',
    'Python is a widely used high-level, general-purpose, interpreted, dynamic programming language.',
    'Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in
    fewer lines of code than possible in languages such as C++ or Java.', 'Python supports multiple programming
    paradigms, including object-oriented, imperative and functional programming or procedural styles.',
    'It features a dynamic type system and automatic memory management and has a large and comprehensive standard
    library.', 'The best way we learn anything is by practice and exercise questions. We  have started this section
    for those (beginner to intermediate) who are familiar with Python.'
]

"""

__in_f1_path = "001.txt"
__in_f2_path = "007.txt"


def main():
    f1 = open(__in_f1_path)
    f2 = open(__in_f2_path)

    lst = f1.read().splitlines(keepends=False) + f2.read().splitlines(keepends=False)

    f1.close()
    f2.close()

    print(lst)


if __name__ == "__main__":
    main()
