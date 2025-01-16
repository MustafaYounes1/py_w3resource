"""

Write a Python class Inventory that would keep track of some items, where each has (id, name, count, price)
The class should support adding, updating (count and price), and checking (given the item id) the item details

=====
ToDo:
=====

1. Add the following items:
    "I001", "Laptop", 100, 500.00
    "I002", "Mobile", 110, 450.00
    "I003", "Desktop", 120, 500.00
    "I004", "Tablet", 90, 550.00

2. Update the item I001 count and price to: 100, 505.00 and check its details

3. Update the item I003 count and price to: 115, 500.00 and check its details

Name: Laptop    , Count: 100, Price:  505.0
Name: Desktop   , Count: 115, Price:  500.0

"""

from dataclasses import dataclass
from typing import Dict


@dataclass
class InventoryItem:
    name: str
    count: int
    price: float


class Inventory:
    def __init__(self):
        self.__depo: Dict[str, InventoryItem] = {}

    def add_item(self, it_id: str, it_name: str, it_count: int, it_price: float) -> None:
        assert it_id not in self.__depo, f"The ID: {it_id} exists already in the depository!"
        self.__depo[it_id] = InventoryItem(it_name, it_count, it_price)

    def update_item(self, it_id: str, it_count: int, it_price: float) -> None:
        assert it_id in self.__depo, f"The item with the ID of: {it_id} doesn't exist in the depository!"
        self.__depo[it_id].count = it_count
        self.__depo[it_id].price = it_price

    def check_details(self, it_id: str) -> None:
        assert it_id in self.__depo, f"The item with the ID of: {it_id} doesn't exist in the depository!"
        print(f"Name: {self.__depo[it_id].name:10}, Count: {self.__depo[it_id].count:3}, "
              f"Price: {self.__depo[it_id].price:6,}")


def main():
    inv = Inventory()

    inv.add_item("I001", "Laptop", 100, 500.00)
    inv.add_item("I002", "Mobile", 110, 450.00)
    inv.add_item("I003", "Desktop", 120, 500.00)
    inv.add_item("I004", "Tablet", 90, 550.00)

    inv.update_item("I001", 100, 505.00)
    inv.check_details("I001")

    inv.update_item("I003", 115, 500.00)
    inv.check_details("I003")


if __name__ == "__main__":
    main()
