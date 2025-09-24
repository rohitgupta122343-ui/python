
my_list = [1,2,3,4,5,6,7,8]

print("Original list: ",my_list)

#        1 , 2 , 3 , 4 , 5 , 6 , 7 , 8
# index  0 , 1 , 2 , 3 , 4 , 5 , 6 , 7
 
# slicing [start : stop : skip]

print(my_list[1:3])      
# [start : stop] --> [1:3]  --->  [2,3]  [stop] --> Low 1 

print(my_list[2::])
# [start : stop : skip] ---> [2::]  -->  [3,4,5,6,7,8]

print(my_list[1:7:2])
# [start : stop : skip] ---> [1:7:2]  -->  [2,4,6] 

print(my_list[1::2])
# [start : stop : skip] --> [1::2]  --->  [2,4,6,8]

print(my_list[::2])
# [start : stop : skip] --> [1:3]  --->  [1,3,5,7]


