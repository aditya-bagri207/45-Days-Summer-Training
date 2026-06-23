import numpy as np

arr1 = np.linspace(1, 10, 5)

arr2 = np.zeros(5)

arr3 = np.ones(5)

final_array = np.vstack((arr1, arr2, arr3))

print("Linspace Array:")
print(arr1)

print("\nZeros Array:")
print(arr2)

print("\nOnes Array:")
print(arr3)

print("\nFinal Stacked Array:")
print(final_array)