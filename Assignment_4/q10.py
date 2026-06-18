try:
    file = open("numbers.txt", "r")

    numbers = list(map(int, file.read().split()))

    total = sum(numbers)

    average = total / len(numbers)

    print("Total =", total)
    print("Average =", average)

    file.close()

except FileNotFoundError:
    print("File does not exist")