"""

Write a Python function that takes a namedtuple as input of the item's name and price. Returns the item's name and price.

Item(name="Mobile", price=300.00)
Item(name="Desktop", price=1500.00)
Item(name="Laptop", price=1200.00)

"""

from typing import Callable, NamedTuple

class Item(NamedTuple):
    name: str
    price: float


def main():
    data = [
        ["Mobile", 300.00],
        ["Desktop", 1500.00],
        ["Laptop", 1200.00],
    ]

    items = [Item(*itm_data) for itm_data in data]
    func: Callable[[Item], tuple[str, int]] = lambda it: (it.name, it.price)

    for item in items:
        print(func(item))


if __name__ == "__main__":
    main()
