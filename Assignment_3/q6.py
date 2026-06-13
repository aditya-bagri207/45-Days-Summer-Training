class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Balance after deposit:", self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        print("Balance after withdrawal:", self.balance)

acc = BankAccount("Aditya", 10000)

acc.deposit(2000)
acc.withdraw(1500)