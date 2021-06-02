from classes.account import Account


class CheckingAccount(Account):
    def __init__(self, id, balance):
        super().__init__(id, balance)
        self.check_uses = 0

    def withdraw(self, amount_to_withdraw):
        withdrawl_fee = 1
        if self.balance - amount_to_withdraw - withdrawl_fee < 0:
            print("Cannot withdraw that amount.")
        else:
            self.balance -= amount_to_withdraw - withdrawl_fee
        return self.balance

    def withdraw_using_check(self, amount_to_withdraw):
        withdrawl_fee = 2 if self.check_uses > 3 else 0
        if self.balance - amount_to_withdraw - withdrawl_fee < -10:
            print("Cannot withdraw that amount.")
        else:
            self.balance -= amount_to_withdraw - withdrawl_fee
        self.check_uses += 1
        return self.balance

    def reset_checks(self):
        self.check_uses = 0
