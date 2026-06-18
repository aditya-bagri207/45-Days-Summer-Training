try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Division =", num1 / num2)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input type")