
#  Write a program to accept a number from the user display sum of
# its digits.


# python way 

n = input("Enter a no ")

total = 0 

for digit in n:
    if digit.isdigit():
        total = total + int(digit)

print("Sum is : ",total)       


                # --- c,c++ way (only Logic) --- 

def check(n):
    sum = 0

    while n != 0:

        r = n % 10
        sum = sum + r
        n = n/10

    return sum     


n = int(input("enter a no : "))

ans = check(n)

print("sum is ",int(ans))
