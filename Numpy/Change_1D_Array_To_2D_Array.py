

# How do you reshape a 1D array into a 2D array?

import numpy as np 

arr_1D = np.array([1,2,3,4,5,6,7,8,9]) # 1D Array 

arr_2d = arr_1D.reshape(3,3) # reshape 3 row and 3 coloums 
   
print(arr_2d)