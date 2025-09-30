
person = {
    "name" : "rohit",
    "age" : 19,
    "city" : "mumbai"
}

print("Dict: ",person)

# Dictionary Method 
# 1 . dict.get()
# 2. dict.keys()
# 3. dict.values()
# 4. dict.items()
# 5. dict.update 
# 6. dict.copy()
# 7. dict.clear()


# 1 . dict.get()

print(f"get: {person.get("name")}")

# 2. dict.keys()

print(f"Keys: {person.keys()}")

# 3. dict.values()

print(f"Values: {person.values()}")

# 4. dict.items()

print(f"Items: {person.items()}")

# 5. dict.update 

person.update({"name" : "rahul"})
print(f"Update: {person}")

# 6. dict.copy()

copy_dict = person.copy()
print("copy ",copy_dict)

# 7. dict.clear()

person.clear()
print("clear: ",person)