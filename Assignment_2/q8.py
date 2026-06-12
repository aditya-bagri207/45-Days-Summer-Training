data = (5, 10, 15, 20, 25, 30, 35)

count = 0

for num in data:
    if num % 5 == 0:
        count += 1

print("Count divisible by 5:", count)
print("Sum of elements:", sum(data))
print("Average:", sum(data) / len(data))