class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited ${amount}. New balance: ${self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.__balance}")

    def get_balance(self):
        return self.__balance

# Usage
acc = BankAccount("John Doe")
acc.deposit(500)
acc.withdraw(200)
print(f"Final Balance: ${acc.get_balance()}")
