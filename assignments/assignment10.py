import numpy as np

# Create a one-dimensional array from 1 to 10
arr = np.arange(1, 11)

print("Original Array:")
print(arr)

# Slicing operations
print("\nSlicing Operations:")
print("First 5 elements:", arr[:5])
print("Elements from index 2 to 6:", arr[2:7])
print("Last 3 elements:", arr[-3:])

# Statistical measures
print("\nStatistical Measures:")
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# Broadcasting to modify array elements
arr = arr + 5

print("\nArray after Broadcasting (adding 5):")
print(arr)
