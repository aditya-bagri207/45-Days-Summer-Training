numbers = [2, 5, 8, 11, 13, 15, 17, 20]

print("Prime numbers are:")

for num in numbers:
    if num > 1:
        prime = True

        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

        if prime:
            print(num)