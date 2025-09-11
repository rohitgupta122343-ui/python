
# Original list
arr1 = [1, 2, 3, 4, 5]

# Aliasing
arr2 = arr1

# Copying
arr3 = arr1[:]

print("Orginal array ",arr1)

arr2[0] = 100
print("aliasing array ",arr2)

arr3[1] = 99
print("copy array ",arr3) 

