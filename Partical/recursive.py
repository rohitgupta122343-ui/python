
# Write a recursive function to print the factorial for a given number.

# factorial e.g 
def factorial(n):
    if n == 0 | n == 1: 
        return 1
    
    else:
        return n * factorial(n-1) 
    

num = 5
print("The Factorial is : ",factorial(5))


# Sum 1 to 100 Without using loop

def recursive_sum(n):

    if n > 100:
        return 0
    else:
       
        return n + recursive_sum(n+1)
    

print(recursive_sum(1))    
