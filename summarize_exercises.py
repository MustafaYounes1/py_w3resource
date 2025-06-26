"""

Use this script to summarize the questions from the exercises' scripts in a certain exercises group that is present
in a dedicated subdirectory.

It would fetch the questions of all exercises (the '*.py' files) and write them down in a text file namely: "000.txt"
that would get created inside the input directory.

Note:   the python scripts are supposed to have a docstring at the beginning that holds the question.
        Best practice would be to create the python scripts with 'create_template_scripts.py'  and then use this
        script to summarize a certain group of exercises.

"""

import argparse
from common import ArgRaTeDeHelpFormatter, fetch_file_doc_string, validate_dir_path


def main(args: argparse.Namespace):
    py_files = [_ for _ in sorted(args.group_dir.iterdir()) if _.suffix == ".py"]
    assert py_files, f"{args.group_dir} has no python scripts"

    out_txt = args.group_dir / "000.txt"
    assert not out_txt.is_file(), f"{out_txt} already exists"

    out_str = ""

    for idx, file in enumerate(py_files):
        docstring = fetch_file_doc_string(file)
        assert docstring, f"{file} has no docstring"

        out_str += "-" * 15 + "\n"
        out_str += f" Exercise: {file.stem}\n"
        out_str += "-" * 15 + "\n\n"
        out_str += docstring + "\n\n"
        out_str += "=" * 78 + "\n"

    with open(out_txt, "w", encoding="utf8") as f:
        f.write(out_str)


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=ArgRaTeDeHelpFormatter
    )

    arg_parser.add_argument(
        "group_dir",
        type=validate_dir_path,
        help="The path to the directory that holds the python scripts of the exercises to be summarized."
    )

    arguments = arg_parser.parse_args()

    main(arguments)
