
# Write a program to perform slicing, basic and advanced indexing on NumPy array

import numpy as np

arr = np.array([1,2,3,4,5])

## basic slicing
print("Original Array :",arr) 
print("arr[1:4]: ",arr[1:4])
print("arr[0:2]: ",arr[0:2])


# basic indexing 
print("Element at index 2 : ",arr[2])
print("Element at index 4 : ",arr[4])


# Advance Indexing 

idx = [0,3,4]

print("Advance Indexing idx[0,3,4] : ",arr[idx])