"""

Write a Python class Restaurant that represents a restaurant with predefined number of tables, menu (food with
its price), and would maintain an orders list and table reservations for customers

=====
ToDo:
=====

1. Create a restaurant that has only 5 tables

2. add the following items to the restaurant menu:
    "Cheeseburger", 9.99
    "Caesar Salad", 8
    "Grilled Salmon", 19.99
    "French Fries", 3.99
    "Fish & Chips:", 15

3. Book table1 and table2 and table3

4. print the current food menu

5. add the following customer orders (where the first number is the table number and the second one is the food from
   the restaurant menu)
        1, "Cheeseburger"
        1, "Grilled Salmon"
        2, "Fish & Chips"
        2, "Grilled Salmon"

6. print the status of tables' availability along with the orders on each table.

Table: 1, Booked/busy:  1, Orders: Cheeseburger, Grilled Salmon
Table: 2, Booked/busy:  1, Orders: Fish & Chips, Grilled Salmon
Table: 3, Booked/busy:  1, Orders:
Table: 4, Booked/busy:  0, Orders:
Table: 5, Booked/busy:  0, Orders:

"""

from collections import defaultdict, OrderedDict
import typing


class Restaurant:
    def __init__(self, n_tables: int):
        self.__fd_menu: typing.OrderedDict[str, float] = OrderedDict()
        self.__tb_busy: typing.OrderedDict[int, bool] = OrderedDict(
            zip(range(1, n_tables + 1), [False] * n_tables)
        )
        self.__ord_lst: typing.DefaultDict[int, typing.List[str]] = defaultdict(list)

    def add_fd_item(self, it_name: str, it_price: float) -> None:
        self.__fd_menu[it_name] = it_price

    def update_table(self, tb_num: int, booked: bool) -> None:
        self.__tb_busy[tb_num] = booked
        if not booked:
            self.__ord_lst[tb_num].clear()

    def get_orders(self, tb_num: int, item_lst: typing.List[str]) -> None:
        assert self.__tb_busy[tb_num], f"Looks like the table {tb_num} is free now!"
        self.__ord_lst[tb_num] += item_lst

    def show_tables_info(self) -> None:
        for tb_n, tb_s in self.__tb_busy.items():
            tb_orders = ", ".join(self.__ord_lst[tb_n])
            print(f"Table: {tb_n}, Booked/busy: {tb_s:2}, Orders: {tb_orders}")


def main():
    r = Restaurant(5)

    r.add_fd_item("Cheeseburger", 9.99)
    r.add_fd_item("Caesar Salad", 8)
    r.add_fd_item("Grilled Salmon", 19.99)
    r.add_fd_item("French Fries", 3.99)
    r.add_fd_item("Fish & Chips", 15)

    r.update_table(1, True)
    r.update_table(2, True)
    r.update_table(3, True)

    r.get_orders(1, ["Cheeseburger", "Grilled Salmon"])
    r.get_orders(2, ["Fish & Chips", "Grilled Salmon"])

    r.show_tables_info()


if __name__ == "__main__":
    main()
