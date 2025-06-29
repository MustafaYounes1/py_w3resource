"""

This script aggregates and summarizes problem statements from a collection of Python exercise scripts located within a
specified directory. It scans all `.py` files in the input directory, extracts the docstring from each file — expected
to contain the exercise's problem statement — and compiles them into a single text file named `000.txt`, which is generated
in the same directory.

Note:   For best results, exercise scripts should be created in advance using `create_template_scripts.py`.
        After filling the template scripts with the problems' definition and their solutions, this script can then be
        used to produce a centralized summary of all exercise questions within the group, facilitating efficient reference
        and review.

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
