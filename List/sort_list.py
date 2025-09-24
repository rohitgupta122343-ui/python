

my_list = [5, 2, 9, 1, 7]

# sort list with using sort function in ascending order
my_list.sort()

print("Ascending ",my_list)

# sort list with using sort function in decending order
my_list.sort(reverse=True)

print("Decending ",my_list)

# using a sorted function 

original_list = [5, 2, 9, 1, 7]

asc_sorted = sorted(original_list)
dsc_sorted = sorted(original_list)

print("Ascending (using sorted) ",asc_sorted)
print("Decending (using sorted) ",dsc_sorted)
print("Original List after: ",original_list)