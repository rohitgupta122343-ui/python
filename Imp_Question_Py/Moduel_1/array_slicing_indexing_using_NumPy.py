
import numpy as np

arr = np.array([1,2,3,4,5])

print("Original  Array: ",arr)

# ---- indexing -----
print("array index 0 ",arr[0])
print("array index 3 ",arr[3])
print("array index 1 ",arr[1])
print("array index -1 ",arr[-1])


print("\nSlicing the array:")
print("arr[1:4] =>", arr[1:4])   
print("arr[:3] =>", arr[:3])     
print("arr[::2]=>",arr[::2])