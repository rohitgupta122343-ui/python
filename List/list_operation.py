


list = [55, 2, 11, 7, 9, 13]
list2 = [1]

# list All operations

list.append(99)            # list = [55, 2, 11, 7, 9, 13, 99]
list.remove(55)            # list = [2, 11, 7, 9, 13, 99]
list.extend(list2)  # list = [2, 11, 7, 9, 13, 99, 1]
list.sort()                # list = [1, 2, 7, 9, 11, 13, 99]
list.sort(reverse=True)    # list = [99, 13, 11, 9, 7, 2, 1]
list.reverse()             # list = [1, 2, 7, 9, 11, 13, 99]
list.pop(1)                # removes 2; list = [1, 7, 9, 11, 13,99]
list.insert(0, 100)        # list = [100, 1, 2, 7, 9, 11, 13]
ans = len(list)            # ans = 7

print(list)
print("len ", ans)

