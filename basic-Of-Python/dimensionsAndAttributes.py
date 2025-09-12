
# Write a program to analyze dimensions and attributes of arrays

import numpy as np 

# Create a 2D array

arr = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print("Array:\n",arr)
print("\n--Array Attributes--\n")

print("Array Shape ",arr.shape)
print("Array Size: ",arr.size)
print("Dimension: ",arr.ndim)
print("Type: ",arr.dtype)
