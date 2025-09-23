#  Create an array (list) of integers
arr = [10, 20, 30, 40, 50]
print("Initial array:", arr)

#  Insert an element at the end
arr.append(60)
print("After inserting 60 at the end:", arr)

#  Insert an element at a specific position (e.g., index 2)
arr.insert(2, 25)  # Inserts 25 at position 2
print("After inserting 25 at index 2:", arr)

# Delete an element by value (e.g., 40)
arr.remove(40)
print("After deleting value 40:", arr)

#  Delete an element by index (e.g., index 1)
del arr[1]
print("After deleting element at index 1:", arr)

#  Traverse the array
print("Traversing the array:")
for element in arr:
    print(element)
