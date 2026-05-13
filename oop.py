class Account:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount
            print(f"Deposit of {amount} successful. New balance: {self.__balance}")

        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):

        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self.__balance}")

        else:
            print("Invalid withdrawal amount or insufficient funds")

    def display_balance(self):
        print(f"{self.owner}'s balance is: {self.__balance}")

    # Getter method for balance
    def get_balance(self):
        return self.__balance

    # Setter method for balance
    def set_balance(self, value):
        self.__balance = value


class Savings(Account):

    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)

        self.interest_rate = 0.02
        self.withdraw_limit = 100

    def apply_interest(self):

        interest = self.interest_rate * self.get_balance()

        new_balance = self.get_balance() + interest

        self.set_balance(new_balance)

        print(f"Interest of {interest} applied")

    # Overriding withdraw method
    def withdraw(self, amount):

        if amount > self.withdraw_limit:

            print(f"Withdrawal cannot exceed {self.withdraw_limit}")

        else:
            super().withdraw(amount)


# Testing

acc1 = Savings("Richard", 500)

acc1.display_balance()

acc1.deposit(200)

acc1.withdraw(50)      # Allowed

acc1.withdraw(150)     # Blocked

acc1.apply_interest()

acc1.display_balance()
