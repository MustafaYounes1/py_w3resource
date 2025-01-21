"""

Write a Python program to create a class representing a bank.

The bank would open accounts for customers, where each account is characterized by an ID and would have a certain
balance. The bank should provide methods for depositing/withdrawing money in/from the user account, and checking their
balance.

bank.open_account("SB-123", 1000)
bank.open_account("SB-124", 1500)

bank.deposit("SB-123", 600)
bank.withdraw("SB-124", 350)

Balance in 'SB-123': 1600
Balance in 'SB-124': 1150

"""


class Bank:
    def __init__(self):
        self.__db: dict[str, float] = {}

    def open_account(self, acc_id: str, init_balance: float) -> None:
        """Open a new account"""
        if acc_id in self.__db:
            raise KeyError(f"'{acc_id}' already opened")

        self.__db[acc_id] = init_balance

    def close_account(self, acc_id: str) -> None:
        """Close an existing account"""
        if acc_id not in self.__db:
            raise KeyError(f"no account with an ID: '{acc_id}' exists")

        del self.__db[acc_id]

    def deposit(self, acc_id: str, amount: float) -> None:
        """Make a deposit"""
        if acc_id not in self.__db:
            raise KeyError(f"no account with an ID: '{acc_id}' exists")

        self.__db[acc_id] += amount

    def withdraw(self, acc_id: str, amount: float) -> None:
        """Make a withdrawal"""
        if acc_id not in self.__db:
            raise KeyError(f"no account with an ID: '{acc_id}' exists")

        if self.__db[acc_id] - amount < 0:
            raise ValueError(f"no enough balance in '{acc_id}'")

        self.__db[acc_id] -= amount

    def check_balance(self, acc_id: str) -> float:
        """Check the balance"""
        if acc_id not in self.__db:
            raise KeyError(f"no account with an ID: '{acc_id}' exists")

        return self.__db[acc_id]


def main():
    bank = Bank()

    bank.open_account("SB-123", 1000)
    bank.open_account("SB-124", 1500)

    bank.deposit("SB-123", 600)
    bank.withdraw("SB-124", 350)

    print(f"Balance in 'SB-123': {bank.check_balance('SB-123')}")
    print(f"Balance in 'SB-124': {bank.check_balance('SB-124')}")


if __name__ == "__main__":
    main()
