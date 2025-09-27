
# Original list

list =[10, 5, 8, 3, 15, 2]
print(" Original list",list)

# Ascending order 
list.sort()
print("Ascending order using sort(): ",list)

# Decending order
list.sort(reverse=True)
print("Decending order using sort(reverse = True) ",list)

original_list = [10, 5, 8, 3, 15, 2]

ascending_order = sorted(original_list)
decending_order = sorted(original_list,reverse=True)

print("Orginal list: ",original_list)
print("Ascending oredr using sorted(): ",ascending_order)
print("Decending order using soretd(): ",decending_order)
