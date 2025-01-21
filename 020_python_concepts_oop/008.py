"""

Write a Python program to create a class representing a shopping cart.

Each item in the shopping cart would have a: name, count, and price

Include methods for:
    Adding an item
    Adding a group of items
    Removing a single item given its name
    Removing a group of items given their name
    Calculating the price of all items in the shopping cart

sh = ShoppingCart()

sh.add_item("chicken", 1, 50)
sh.add_items(
    [
        ("milk", 1, 25),
        ("soda", 2, 15.5),
        ("bread", 4, 10)
    ]
)

sh.get_price        =>  146.0

sh.remove_item("milk")
sh.remove_items(["soda", "chicken"])

sh.get_price        =>  40

"""

from dataclasses import dataclass


@dataclass
class Item:
    name: str
    count: int
    price: int | float


class ShoppingCart:
    def __init__(self):
        self.__items: list[Item] = []

    def add_item(self, name: str, count: int, price:  int | float) -> None:
        """Add a single item"""
        self.__items.append(Item(name, count, price))

    def add_items(self, items: list[tuple[str, int, int | float]]) -> None:
        """Add a group of items"""
        for item in items:
            self.add_item(*item)

    def remove_item(self, name: str) -> None:
        """Remove a single item given its name"""
        self.__items = list(filter(lambda i: i.name != name, self.__items))

    def remove_items(self, names: list[str]) -> None:
        """Remove a group of items given their names"""
        self.__items = list(filter(lambda i: i.name not in names, self.__items))

    @property
    def get_price(self) -> int | float:
        """Get the total price of all items in the shopping cart"""
        return sum(_.price * _.count for _ in self.__items)


def main():
    sh = ShoppingCart()

    sh.add_item("chicken", 1, 50)
    sh.add_items(
        [
            ("milk", 1, 25),
            ("soda", 2, 15.5),
            ("bread", 4, 10)
        ]
    )

    print(sh.get_price)

    sh.remove_item("milk")
    sh.remove_items(["soda", "chicken"])

    print(sh.get_price)


if __name__ == "__main__":
    main()
