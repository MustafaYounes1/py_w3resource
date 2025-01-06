"""

Write a Python program to find the location of Python module sources.

e.g.: try to find the location of the 'os' and 'datetime' libraries

"""

import importlib.util


def find_module_location(module_name):
    # Find the spec for a module, optionally relative to the specified package name.
    spec = importlib.util.find_spec(module_name)

    # Name of the place from which the module is loaded, e.g. “builtin” for built-in modules and the filename for
    # modules loaded from source.
    if spec and spec.origin:
        return spec.origin
    else:
        return f"Module '{module_name}' not found."


def main():
    # Find the location of 'os' and 'datetime'
    os_location = find_module_location('os')
    datetime_location = find_module_location('datetime')

    # Print the results
    print(f"Location of 'os' module: {os_location}")
    print(f"Location of 'datetime' module: {datetime_location}")


if __name__ == "__main__":
    main()
