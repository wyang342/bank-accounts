from classes.account import Account


class SavingsAccount(Account):
    def __init__(self, id, balance):
        self.id = id
        self.balance = 0
        if balance < 10:
            raise Exception
        else:
            self.balance = balance

    def withdraw(self, amount_to_withdraw):
        withdrawl_fee = 2
        if self.balance - amount_to_withdraw - withdrawl_fee < 10:
            print("Cannot withdraw that amount.")
        else:
            self.balance -= amount_to_withdraw - withdrawl_fee
        return self.balance

    def add_interest(self, rate):
        interest = self.balance * rate / 100
        self.balance += interest
        return interest
