
student = {
    "name" : "rohit",
    "age" : 19
}

print("Dict: ",student)

# Dictionary Method 
# 1 . dict.get()
# 2. dict.keys()
# 3. dict.values()
# 4. dict.items()
# 5. dict.update 
# 6. dict.copy()
# 7. dict.clear()


# 1 . dict.get()

print(f"get: {student.get("name")}")

# 2. dict.keys()

print(f"Keys: {student.keys()}")

# 3. dict.values()

print(f"Values: {student.values()}")

# 4. dict.items()

print(f"Items: {student.items()}")

# 5. dict.update 

student.update({"name" : "rahul"})
print(f"Update: {student}")

# 6. dict.copy()

copy_dict = student.copy()
print("copy ",copy_dict)

# 7. dict.clear()

student.clear()
print("clear: ",student)

