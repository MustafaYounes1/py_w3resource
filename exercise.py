"""

Practice and improve your skills by solving randomized exercises using this tool.

"""

import argparse
from common import ArgRaTeDeHelpFormatter, EXCLUDED_DIRS, fetch_file_doc_string, validate_dir_path
import pathlib
import random
from typing import Callable, Generator


def main(args: argparse.Namespace):
    assert args.num_exercises > 0, "args.num_exercises should be greater than zero"

    if args.seed is not None:
        random.seed(args.seed)

    get_py_files: Callable[[pathlib.Path], list[pathlib.Path]] = lambda d: [_ for _ in d.iterdir() if _.suffix == ".py"]

    py_files = []
    # the default sources: all subdirectories in the current file directory
    if args.sources == pathlib.Path(__file__).parent:
        for p in args.sources.iterdir():
            if p.is_dir() and p not in EXCLUDED_DIRS:
                py_files += get_py_files(p)
    
    # the sources provided by the user
    else:
        for p in args.sources:
            py_files += get_py_files(p)

    assert py_files, f"Couldn't find any python scripts in {args.sources}"
    if len(py_files) < args.num_exercises:
        print(f"\033[91mWARNING\033[0m: the provided sources only contain {len(py_files):,} exercises.")

    random.shuffle(py_files)  # shuffle the exercises
    exercises_prompts_getter: Generator[tuple[pathlib.Path, str], None, None] = (
        (f, fetch_file_doc_string(f)) for f in py_files
    )

    n, max_exr_id = 0, min(len(py_files), args.num_exercises)
    if max_exr_id > 1:
        print("\033[33mINFO\033[0m: press \033[32mEnter\033[0m to move on to the next exercise, or \033[31mc\033[0m to "
              "exit.")

    print()

    while n < max_exr_id:

        # provide the ability to pause between exercises until the user press 'Enter' to move on or 'c' to exit.
        if n:
            while k := input():
                if k.lower() == "c":
                    raise SystemExit(0)

        f, exr_prompt = next(exercises_prompts_getter)

        # continue if the docstring couldn't be parsed
        if not exr_prompt:
            continue

        n += 1
        id_txt = f" {n:,}/{max_exr_id:,} "
        print(f"\033[1m{id_txt:=^120}\033[0m")
        print(f"\n{exr_prompt}\n")
        print(f"\n\033[92mSolution\033[0m: {f}")


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=ArgRaTeDeHelpFormatter
    )

    arg_parser.add_argument(
        "-n",
        "--num_exercises",
        type=int,
        default=1,
        help="Number of random exercises to fetch."
    )

    arg_parser.add_argument(
        "-src",
        "--sources",
        type=validate_dir_path,
        default=pathlib.Path(__file__).parent,
        nargs="+",
        help="Source groups from which the random exercises would be fetched. \nBy default, all subdirectories present in "
             "the current file directory would be considered as source groups."
    )

    arg_parser.add_argument(
        "-s",
        "--seed",
        type=int,
        default=None,
        help="Seed optional argument for reproducibility."
    )

    arguments = arg_parser.parse_args()

    main(arguments)
