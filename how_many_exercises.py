"""

Count how many exercises you have completed so far.

By default, it would count all '*.py' files in all subdirectories where each python script is supposed to hold
the solution for a certain exercise. However, it's possible to count how many exercises have been completed in just one
single subdirectory that is existed in the root directory by providing the subdirectory name

"""

import argparse
from collections import OrderedDict
import pathlib


__excluded_dirs = [".git", ".idea"]


def main(args):
    if args.dir == pathlib.Path():
        stats = OrderedDict()
        total = 0

        for p in args.dir.iterdir():
            if p.is_dir() and str(p) not in __excluded_dirs:
                py_files = [f for f in p.iterdir() if f.suffix == ".py"]
                stats[str(p)] = len(py_files)
                total += len(py_files)

        print(f"You have completed {total:,} exercises so far!\n")

        for k, v in stats.items():
            print(f"You completed {v:3,} in {k}")

    else:
        curr_dir = pathlib.Path(__file__).cwd()
        assert args.dir.resolve().parent == curr_dir, f"{args.dir} does not exist in {curr_dir}"
        py_files = [f for f in args.dir.iterdir() if f.suffix == ".py"]
        print(f"You have completed {len(py_files):,} exercises in '{args.dir}'")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "--dir",
        type=pathlib.Path,
        default=pathlib.Path(),
        help="By default it would recursively walk through all subdirectories in the current file directory and count "
             "all '*.py' files where each python script is supposed to hold the solution for a certain exercise. "
             "\nHowever, with this argument it's possible to provide a name of a certain subdirectory that is assumed "
             "to be present in the current directory and it would count all '*.py' in it."
    )

    arguments = parser.parse_args()

    main(arguments)
