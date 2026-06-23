import numpy as np

arr1 = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

arr2 = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

addition = arr1 + arr2
print("Addition: ")
print(addition)


Subtraction = arr1 - arr2
print("Subtraction: ")
print(Subtraction)


multiplication = np.dot(arr1, arr2)  #multiplication = arr1 @ arr2 ,,  this is also use for multiplication
print("Multiplication: ")
print(multiplication)