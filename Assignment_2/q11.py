def find_duplicates(arr):
    duplicates = set()

    for num in arr:
        if arr.count(num) > 1:
            duplicates.add(num)

    print("Duplicate elements are:")
    for item in duplicates:
        print(item)

arr = [10, 20, 30, 20, 40, 10, 50, 30]

find_duplicates(arr)