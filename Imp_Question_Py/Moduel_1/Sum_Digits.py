
def digit(n):
    sum = 0

    while n != 0:
        r = n % 10
        sum = sum + r
        n = n // 10

    return sum    

n = int(input("enter a number: "))

print(f"Sum: {digit(n)} ---> {n}")