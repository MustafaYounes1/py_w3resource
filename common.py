"""

This script provides common utilities for the tools present in this repo

"""

import argparse
from itertools import islice
import pathlib
import re
from typing import Any, Iterable, Generator


# the template contents of the exercises' scripts
EXR_SCR_TEMPLATE_CONTENTS = """\"\"\"

Describe the task here

\"\"\"


def main():
    pass


if __name__ == "__main__":
    main()
"""

# Directories that won't be iterated through when counting/getting exercises
EXCLUDED_DIRS = {".git", ".idea", "__pycache__"}


class ArgRaTeDeHelpFormatter(argparse.RawTextHelpFormatter, argparse.ArgumentDefaultsHelpFormatter):
    """argparse help formatter to combine the features of both argparse.RawTextHelpFormatter and
    argparse.ArgumentDefaultsHelpFormatter"""
    ...


def validate_dir_path(d: str) -> pathlib.Path | None:
    """Validate the existence of the 'd' directory. (typically used to validate the directories passed to the CLIs of
    the available tools)"""
    d_path = pathlib.Path(d)

    if d_path.is_dir():
        return d_path
    else:
        raise argparse.ArgumentTypeError(f"{d_path} doesn't exist.")


def fetch_file_doc_string(file: pathlib.Path) -> str:
    """Fetch the doc string from '*.py' files"""
    with open(file, "r", encoding="utf8") as f:
        contents = "".join(f.readlines())
        match = re.match(r'^\s*([\'\"]{3})(.*?)\1', contents, re.DOTALL)

        if match is None:
            return ""
        else:
            return match.group(2).strip()


def batchify(iterable: Iterable[Any], bs: int = 1) -> Generator[tuple[Any, ...], None, None]:
    """Batchify the input iterable into a tuples of size bs. Note that the last batch could be shorter"""
    it = iter(iterable)

    while batch := tuple(islice(it, bs)):
        yield batch
