import os
import csv


class Account:
    def __init__(self, id, balance):
        self.id = id
        self.balance = 0
        if int(balance) < 0:
            raise Exception
        else:
            self.balance = balance

    def withdraw(self, amount_to_withdraw):
        if self.balance - amount_to_withdraw < 0:
            print("Cannot withdraw that amount.")
        else:
            self.balance -= amount_to_withdraw
        return self.balance

    def deposit(self, amount_to_deposit):
        self.balance += amount_to_deposit
        return self.balance

    @classmethod
    def all_accounts(cls):
        proj_path = os.path.abspath(os.getcwd())
        csv_path = os.path.join(proj_path, "../support/accounts.csv")

        with open(csv_path, "r") as csvfile:
            reader = csv.reader(csvfile)
            accounts = []
            for row in reader:
                accounts.append(cls(int(row[0]), int(row[1])))

        return accounts

    @classmethod
    def find(cls, id):
        accounts = cls.all_accounts()
        for account in accounts:
            if account.id == id:
                return account

        return None
