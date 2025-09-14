
# Write a recursive function to print the factorial for a given number.

def factorial(n):
    if n == 0 | n == 1:
        return 1
    
    else:
        return n * factorial(n-1)
    

num = 5
print("The Factorial is : ",factorial(5))