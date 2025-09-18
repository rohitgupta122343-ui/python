
# Write a program that takes two lists and returns True if they have at
# least one common member. 

def check(l1,l2):

    for i in l1:   
        for j in l2:
            if i == j:
                print("The common member is:",j)
                
            
    return -1


list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9] 

print(check(list1,list2))