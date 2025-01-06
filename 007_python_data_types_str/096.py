"""

Write a Python program to convert a given string to Camelcase.

Camel case (sometimes stylized as camelCase or CamelCase; also known as camel caps or more formally as medial
capitals) is the practice of writing phrases without spaces or punctuation, indicating the separation of words with
a single capitalized letter, and the first word starting with either case.

Note: World would come separated in the input using '-' or '_', otherwise it would be only one single word

'JavaScript'        Javascript
'Foo-Bar'           FooBar
'foo_bar'           FooBar
'--foo.bar'         Foo.bar
'Foo-BAR'           FooBar
'fooBAR'            Foobar
'foo bar'           FooBar

"""

import re


def main():
    s = ["JavaScript", 'Foo-Bar', 'foo_bar', '--foo.bar', 'Foo-BAR', 'fooBAR', 'foo bar']
    for _ in s:
        print(
            "".join([__.capitalize() for __ in re.sub("[-|_]+", " ", _).split()])
        )


if __name__ == "__main__":
    main()
