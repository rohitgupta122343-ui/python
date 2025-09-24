
def check(l1,l2):
    
    for i in l1:
        for j in l2:
            if i == j:
                return True,i
            
    return False        

my_list1 = [1,2,3,4,5]
my_list2 = [5,6,7,8,9]

print(check(my_list1,my_list2))