
def fact(n):

    if n == 1:
        return n
    else:
        return n * fact(n-1)

n = int(input("enter a number: "))

print(f"{n} Factorial : {fact(n)}")