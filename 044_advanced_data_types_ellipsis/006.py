"""

Write a Python program that creates a custom class with an 'init' method. Use 'ellipsis' to indicate that some
attributes may be added dynamically.


"""

class TestClass:
    def __init__(self, attr1: ..., attr2: ..., attr3: ..., attr4: ... = ...):
        self._attr1 = attr1
        self._attr2 = attr2
        self._attr3 = attr3
        self._attr4 = attr4

    @property
    def attr1(self) -> ...:
        return self._attr1

    @property
    def attr2(self) -> ...:
        return self._attr2

    @property
    def attr3(self) -> ...:
        return self._attr3

    @property
    def attr4(self) -> ...:
        return self._attr4

    @attr4.setter
    def attr4(self, val: ...) -> None:
        self._attr4 = val


def main():
    c = TestClass(1, "hello", 1.0)

    for attr_name in ("attr1", "attr2", "attr3", "attr4"):
        print(attr_name, getattr(c, attr_name))

    c.attr4 = 10
    print(c.attr4)


if __name__ == "__main__":
    main()
