
def arm(n):
    temp = n
    sum = 0

    while n != 0:
        r = n % 10
        sum = sum + (r*r*r)
        n = n // 10

    return temp == sum    

n = int(input("enter a number: "))

if arm(n):
    print("Armstrong Number: ",n)
else:
    print("Not a Armstrong: ",n)    