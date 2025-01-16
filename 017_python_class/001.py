"""

Write a Python program to import the built-in array module and display the namespace of the said module.

__name__ array
__doc__ This module defines an object type which can efficiently represent
an array of basic values: characters, integers, floating point
numbers.  Arrays are sequence types and behave very much like lists,
except that the type of objects stored in them is constrained.

__package__
__loader__ <class '_frozen_importlib.BuiltinImporter'>
__spec__ ModuleSpec(name='array', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')
_array_reconstructor <built-in function _array_reconstructor>
ArrayType <class 'array.array'>
array <class 'array.array'>
typecodes bBuhHiIlLqQfd

"""

import array


def main():
    for k, v in array.__dict__.items():
        print(k, v)


if __name__ == "__main__":
    main()
