"""

Write a Python program to get the last modified information of a file.

"""

from datetime import datetime
from pathlib import Path


def main():
    print(datetime.fromtimestamp(Path(__file__).stat().st_mtime))


if __name__ == "__main__":
    main()
