"""

Write a Python program to get a list of locally installed Python modules

Hint: use 'importlib' module

"""

import importlib.metadata


def list_installed_modules():
    installed_modules = []

    for dist in importlib.metadata.distributions():
        module_name = dist.metadata["Name"]
        module_version = dist.version
        installed_modules.append((module_name, module_version))

    return installed_modules


def main():
    modules = list_installed_modules()
    for m, v in modules:
        print(f"{m:30s}\t{v:10s}")


if __name__ == "__main__":
    main()
