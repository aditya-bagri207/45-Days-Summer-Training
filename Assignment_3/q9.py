class Calculator:
    def add(self, a, b):
        print("Addition =", a + b)

    def subtract(self, a, b):
        print("Subtraction =", a - b)

    def multiply(self, a, b):
        print("Multiplication =", a * b)

    def divide(self, a, b):
        print("Division =", a / b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

c = Calculator()

c.add(a, b)
c.subtract(a, b)
c.multiply(a, b)
c.divide(a, b)