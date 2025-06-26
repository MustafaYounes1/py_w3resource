"""

Count how many exercises this repo holds so far.

By default, it would count all '*.py' files in all subdirectories where each python script is supposed to hold
the solution for a certain exercise. However, it's possible to count how many exercises exist in just one single
subdirectory that is existed in the root directory by providing the subdirectory name

"""

import argparse
from collections import OrderedDict
from common import ArgRaTeDeHelpFormatter, batchify, EXCLUDED_DIRS, validate_dir_path
import pathlib


def main(args: argparse.Namespace):
    if args.dir == pathlib.Path(__file__).parent:
        stats = OrderedDict()
        total = 0

        for p in args.dir.iterdir():
            if p.is_dir() and p.name not in EXCLUDED_DIRS:
                py_files = [f for f in p.iterdir() if f.suffix == ".py"]
                stats[p.name] = len(py_files)
                total += len(py_files)

        nc, c_sep = 3, " " * 8
        max_l = max(map(len, stats))

        # log the number of exercises in each group
        for batch in batchify(stats, nc):

            for grp in batch:
                print(f"{grp:.<{max_l}} {stats[grp]:>3d}", end=c_sep)

            print()

        print()

        # log the number of total exercises
        max_row_l = nc * (max_l + 4) + len(c_sep) * (nc - 1)
        print(f"Total exercises: {total:,}".center(max_row_l, "."))

    else:
        py_files = [f for f in args.dir.iterdir() if f.suffix == ".py"]
        print(f"'{args.dir}' holds {len(py_files):,} exercises.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=ArgRaTeDeHelpFormatter
    )

    parser.add_argument(
        "-d",
        "--dir",
        type=validate_dir_path,
        default=pathlib.Path(__file__).parent,
        help="By default it would recursively walk through all subdirectories in the current file directory and count "
             "all '*.py' files where each python script is supposed to hold the solution for a certain exercise. "
             "\nHowever, with this argument it's possible to provide a name of a certain subdirectory that is assumed "
             "to be present in the current directory and it would count all '*.py' in it."
    )

    arguments = parser.parse_args()

    main(arguments)
