
    
# Write a program to generate the Fibonacci series.


n = int(input("Enter a no : "))

a = 0
b = 1

# python way 

for i in range(n):
    print(a,end=" ")
    a,b = b, a+b


# c,c++ way (only Logic)
c = a+b

for i in range(n):
    print(a)
    a = b
    b = c
    c = a+b
    