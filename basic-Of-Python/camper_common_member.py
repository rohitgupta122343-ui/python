
# Write a program to compute number of characters and words in a
# string.

def check(l1,l2):

    for i in l1:
        for j in l2:
            if i == j:
                print("The common member is:",j)
                
            
    return -1


list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9] 

print(check(list1,list2))