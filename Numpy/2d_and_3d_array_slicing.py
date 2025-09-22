

import numpy as np 

# 2D Array

arr2D = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print("arr2D[1][0]:",arr2D[1][0])  
# arr2D[1] accesses the second row of the array: --> [4, 5, 6]
# arr2D[1][0] accesses the first element of that row: 4

# 3D Array 

arr3D = [
    
    [[1,2,3],[10,11,12],[13,14,15]],
    [[4,5,6],[16,17,18],[20,21,22]],
    [[7,8,9],[24,25,26],[27,28,29]]
    
]

print("Arr3D[2][1][1]",arr3D[2][1][1])
# arr3D[2] accesses the last row --> [7,8,9] [24,25,26] [27,28,29]
# arr3D[2][1] accesses the ---> [24,25,26]
# arr3D[2][1][1] accesses the --> 25
 