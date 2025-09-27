
# creation
list = ["apple","banana","cherray","orange","date"]

# indexing
print("first fruits: ",list[0])
print("last fruits: ",list[4])

# Slicing

print("list[0:2]: ",list[0:2])
print("list[1:3]: ",list[1:3])
print("list[:4]: ",list[:4])

# modity list also
list[0] = "blueberry"
print("after the changes: ",list)

# add element

list.append("mango")
print("after the append: ",list)

# remove 
list.remove("date")
print("after removing the element: ",list)