"""

Write a Python class BankAccount with attributes like account_number, balance, date_of_opening and customer_name,
and methods like deposit, withdraw, and a method to show the details of the accountr.

=====
ToDo:
=====

1. Add the following accounts:
    BankAccount(2345, "01-01-2011", 1000, "Toninho Takeo")
    BankAccount(1234, "11-03-2011", 2000, "Astrid Rugile")
    BankAccount(2312, "12-01-2009", 3000, "Orli Kerenza")
    BankAccount(1395, "01-01-2011", 3000, "Luciana Chika")
    BankAccount(6345, "01-05-2011", 4000, "Toninho Takeo")

2. Show their details

3. The forth account deposited 500 into his account

4. Check the forth account balance

5. The forth account withdrew 5000 from his account

6. The forth account withdrew 3400 from his account

7. Check the forth account balance

==================================================
ID: 2345
Opened in: 2011-01-01
Balance: 1000
Customer Name: Toninho Takeo
==================================================
ID: 1234
Opened in: 2011-03-11
Balance: 2000
Customer Name: Astrid Rugile
==================================================
ID: 2312
Opened in: 2009-01-12
Balance: 3000
Customer Name: Orli Kerenza
==================================================
ID: 1395
Opened in: 2011-01-01
Balance: 3000
Customer Name: Luciana Chika
==================================================
ID: 6345
Opened in: 2011-05-01
Balance: 4000
Customer Name: Toninho Takeo
==================================================
The balance in the account 1395 is: 3500
The balance in the account 1395 is: 0.0

"""

from datetime import date, datetime


class BankAccount:
    def __init__(self, acc_id: int, acc_date: str, balance: float, cust_name: str):
        self.__id: int = acc_id
        self.__date: date = datetime.strptime(acc_date, "%d-%m-%Y").date()
        self.__balance: float = balance
        self.__cust_name: str = cust_name

    def print_acc_details(self) -> None:
        print(f"ID: {self.__id}\nOpened in: {self.__date}\nBalance: {self.__balance}\nCustomer Name: "
              f"{self.__cust_name}")

    def check_balance(self) -> None:
        print(f"The balance in the account {self.__id} is: {self.__balance}")

    def deposit(self, amount: float) -> None:
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        self.__balance = max(0., self.__balance - amount)


def main():
    b1 = BankAccount(2345, "01-01-2011", 1000, "Toninho Takeo")
    b2 = BankAccount(1234, "11-03-2011", 2000, "Astrid Rugile")
    b3 = BankAccount(2312, "12-01-2009", 3000, "Orli Kerenza")
    b4 = BankAccount(1395, "01-01-2011", 3000, "Luciana Chika")
    b5 = BankAccount(6345, "01-05-2011", 4000, "Toninho Takeo")

    print('=' * 50)
    for b in [b1, b2, b3, b4, b5]:
        b.print_acc_details()
        print('=' * 50)

    b4.deposit(500)
    b4.check_balance()

    b4.withdraw(5000)
    b4.withdraw(3400)
    b4.check_balance()


if __name__ == "__main__":
    main()
