
import numpy as np

arr = np.array([9,18,-7,4,3,-2 ,10,-19])

arr[arr < 0] = 0

print(arr)