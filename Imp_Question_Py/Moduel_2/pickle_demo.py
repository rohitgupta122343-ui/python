import pickle

# pickle is used to store  data types like dict, list, tuple

obj = {
    "name": "rohit",
    "age": 19
}

# Open file in write-binary mode and store (dump) the object
with open("data.pkl", "wb") as file:
    pickle.dump(obj, file)  # Store the object in the specified file location

# Open file in read-binary mode and load the object
with open("data.pkl", "rb") as file:
    loaded = pickle.load(file)  # Load the data from the file to use in the program

print(loaded)  # Display the loaded data
