"""

Use this script to summarize the questions from the exercises' scripts in a certain exercises group.

It would fetch the questions of all exercises and write them in a text file namely: "000.txt" that would get created
inside the input directory.

Note:   the python scripts are supposed to have a docstring at the beginning that holds the question.
        Best practice would be to create the python scripts with 'create_template_scripts.py' python file and then use
        this script to summarize a certain group of exercises

"""

import argparse
import pathlib
import re


def main(args):
    assert args.group_dir.is_dir(), f"{args.group_dir} doesn't exist"

    py_files = [_ for _ in sorted(args.group_dir.iterdir()) if _.suffix == ".py"]
    assert py_files, f"{args.group_dir} has no python scripts"

    out_str = ""

    for idx, file in enumerate(py_files):
        with open(file, "r", encoding="utf8") as f:
            contents = "".join(f.readlines())
            match = re.match(r'^\s*([\'\"]{3})(.*?)\1', contents, re.DOTALL)

            assert match is not None, f"{file} has no docstring"

            docstring = match.group(2).strip()

            out_str += "-" * 15 + "\n"
            out_str += f" Exercise: {file.stem}\n"
            out_str += "-" * 15 + "\n\n"
            out_str += docstring + "\n\n"
            out_str += "=" * 78 + "\n"

    out_txt = args.group_dir / "000.txt"
    assert not out_txt.is_file(), f"{out_txt} already exists"

    with open(out_txt, "w", encoding="utf8") as f:
        f.write(out_str)


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(
        description="Summarize a group of exercises"
    )

    arg_parser.add_argument(
        "group_dir",
        type=pathlib.Path,
        help="The path to the directory that holds the python scripts of the exercises to be summarized."
    )

    arguments = arg_parser.parse_args()
    main(arguments)
