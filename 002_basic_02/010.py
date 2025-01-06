"""
Write a Python program to display some information about the OS where the script is running.

MetaData to show:

    'architecture',
    'linux_distribution',
    'mac_ver',
    'machine',
    'node',
    'platform',
    'processor',
    'python_build',
    'python_compiler',
    'python_version',
    'release',
    'system',
    'uname',
    'version',

Hint: use 'platform' module
Note: not all data above are cross-platform

"""

import platform


def main():
    meta_data = [
        'architecture',
        'linux_distribution',
        'mac_ver',
        'machine',
        'node',
        'platform',
        'processor',
        'python_build',
        'python_compiler',
        'python_version',
        'release',
        'system',
        'uname',
        'version',
    ]

    for p in meta_data:
        if hasattr(platform, p):
            print(f"{p:20s}\t{str(getattr(platform, p)()):10s}")


if __name__ == "__main__":
    main()
