# Title: Basic Array Operations, Indexing, and Slicing in Python


arr = [1,2,3,4,5]

print("Original  Array: ",arr)

# ---------- Indexing ----------
print("\nAccessing elements using indexing:")
print("Array index 0: ",arr[0])
print("Array index 3: ",arr[3])
print("Array index 1: ",arr[1])
print("Last Elment : ",arr[-1])



print("\nSlicing the array:")
print("arr[1:4] =>", arr[1:4])   
print("arr[:3] =>", arr[:3])     
print("arr[::2] =>", arr[::2]) 

print("\nPerforming basic operations:")

# apppend
arr.append(35)
print("After append ",arr)

# pop element at index 2
arr.pop(2)
print("After pop ",arr)

# insert at index 5
arr.insert(4,65)
print("After Insert ",arr)

# Remove a specific element
arr.remove(5)
print("After remove(5):", arr)

# Reverse the array
arr.reverse()
print("Reversed array:", arr)
