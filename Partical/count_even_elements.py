
import numpy as np

arr = np.array([3, 4, 2, 8, 10, 13, 16])

even = (arr %2 == 0)

even_sum = np.sum(even)

print(even_sum)