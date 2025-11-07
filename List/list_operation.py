

list = [55, 2, 11, 7, 9, 13]
list2 = [1, 2, 3]

# List operations
list.append(99)             # list = [55, 2, 11, 7, 9, 13, 99]
list.remove(55)             # list = [2, 11, 7, 9, 13, 99]
list.extend(list2)          # list = [2, 11, 7, 9, 13, 99, 1, 2, 3]
list.sort()                 # list = [1, 2, 2, 3, 7, 9, 11, 13, 99]
list.sort(reverse=True)     # list = [99, 13, 11, 9, 7, 3, 2, 2, 1]
list.reverse()              # list = [1, 2, 2, 3, 7, 9, 11, 13, 99]
val = list.pop(1)           # removes element at index 1 (value 2)
list.insert(0, 100)         # list  -->  [100, 1, 2, 3, 7, 9, 11, 13, 99]


ans = len(list)

print("Final list:", list)
print("Length of list:", ans)
print("Popped value:", val)