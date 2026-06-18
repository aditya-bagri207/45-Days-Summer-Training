class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("Balance:", self.__balance)

    def withdraw(self, amount):
        self.__balance -= amount
        print("Balance:", self.__balance)

acc = BankAccount(10000)

acc.deposit(2000)
acc.withdraw(1500)