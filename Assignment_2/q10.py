def count_frequency(arr):
    for num in set(arr):
        print(num, "->", arr.count(num), "times")

arr = [1, 2, 2, 3, 1, 4, 2]

count_frequency(arr)