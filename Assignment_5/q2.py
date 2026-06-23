import numpy as np

arr = np.array([
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [50, 60, 70, 80],
    [11, 22, 33, 44]
])

print("Original Matrix: ")
print(arr)

diagonal = np.diag(arr)
print("Diagonal element: ")
print(diagonal)

arr[arr % 2 == 0] = 0

print("After Replacing Even Numbers:")
print(arr)

print("Index of Maximum Value:")
print(np.argmax(arr))
