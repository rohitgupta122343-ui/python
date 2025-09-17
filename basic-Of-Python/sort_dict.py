
# Write a Python script to sort (ascending and descending) a dictionary
# by value.

data = {
    "apple" : 2,
    "banana" : 1,
    "cherry" : 4,
    "orange" : 3
}

asc = dict(sorted(data.items(), key = lambda x: x[1]))
desc = dict(sorted(data.items(), key = lambda x: x[1],reverse=True))

print("Assending : ",asc)
print("Descending : ",desc)
