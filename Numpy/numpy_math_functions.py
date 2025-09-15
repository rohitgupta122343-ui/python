
# How do you perform basic mathematical operations (such as max, min, mean, sum, square, sine, and cosine) on a NumPy array in Python?

import numpy as np

arr = np.array([1,2,3,4,5])

print("Original Array: ",arr)

print("Maximum number in array: ",np.max(arr))
print("Minimum number in array: ",np.min(arr))
print("Mean of array: ",np.mean(arr))
print("Sum of array: ",np.sum(arr))
print("Square of each element: ",np.square(arr))

print("Sine of array: ",np.sin(arr))
print("Cosine of array: ",np.cos(arr))