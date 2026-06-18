def calculate(arr):
    even_count = 0
    odd_sum = 0

    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_sum += num

    print("Even Count:", even_count)
    print("Odd Sum:", odd_sum)

numbers = [10, 15, 20, 25, 30]

calculate(numbers)