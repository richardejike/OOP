class Account:

    def __init__(self):
        self.balance = 0
        print("Account balance is:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Account balance is:", self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        print("Account balance is:", self.balance)


class SavingsAccount(Account):

    def __init__(self):
        super().__init__()
        self.withdraw_limit = 100

    def withdraw(self, amount):

        if amount > self.withdraw_limit:
            print("Withdrawal limit exceeded")

        elif amount > self.balance:
            print("Insufficient balance")

        else:
            self.balance -= amount
            print("Account balance is:", self.balance)


acc1 = SavingsAccount()

acc1.deposit(200)

acc1.withdraw(70)

acc1.withdraw(150)
