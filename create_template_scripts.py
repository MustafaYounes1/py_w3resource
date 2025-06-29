"""

A tool to automate the creation of multiple template scripts for many exercises at once. The name of each resultant
script would refer to the exercise ID, and its contents would be the following template:

\"""

Describe the task here

\"""


def main():
    pass


if __name__ == "__main__":
    main()

"""

import argparse
from common import ArgRaTeDeHelpFormatter, EXR_SCR_TEMPLATE_CONTENTS
import pathlib
from tqdm import tqdm


__digit_len = 3


def main(args: argparse.Namespace):
    assert args.first_exc_id > 0, "args.first_exc_id should be greater than zero"
    assert args.last_exc_id > 0, "args.last_exc_id should be greater than zero"
    assert args.last_exc_id >= args.first_exc_id, ("Last exercise ID should be equal to or greater than the First "
                                                   "exercise ID.")

    for scr_id in tqdm(
            range(args.first_exc_id, args.last_exc_id + 1),
            total=args.last_exc_id - args.first_exc_id + 1,
            desc="Creating template scripts: ",
            unit="script"
    ):
        args.out_dir.mkdir(exist_ok=True)
        out_f = args.out_dir / f"{str(scr_id).zfill(3)}.py"
        assert not out_f.is_file(), f"{str(out_f)} already exists"
        with open(out_f, "w") as f:
            f.write(EXR_SCR_TEMPLATE_CONTENTS)


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=ArgRaTeDeHelpFormatter
    )

    arg_parser.add_argument(
        "first_exc_id",
        type=int,
        help="The first exercise ID"
    )

    arg_parser.add_argument(
        "last_exc_id",
        type=int,
        help="The last exercise ID, must be equal to or greater than 'first_exc_id'"
    )

    arg_parser.add_argument(
        "out_dir",
        type=pathlib.Path,
        help="The output directory where the template scripts would be created."
    )

    arguments = arg_parser.parse_args()

    main(arguments)
