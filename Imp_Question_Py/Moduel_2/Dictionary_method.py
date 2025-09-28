
student = {
    "name": "rohit",
    "age": 19
}


print(student.get("name"))

print(student.keys())
print(student.values())
print(student.items())

# Update the dictionary
student.update({"name": "king"})
print(student)

# Copy the dictionary
copy = student.copy()
print(copy)

# Clear the dictionary
student.clear()
print(student)
