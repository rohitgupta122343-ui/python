
def amg(n):

    ## c,c++ way (logic only)

    sum = 0
    temp = n

    while n != 0:
          r = n%10
          sum = sum + (r*r*r)
          n = n//10


    if sum == temp:
         return True
    else:
         return False 
    
    ## python way 
    
    # sum = 0
    # digits = str(n)
    # power = len(digits)
    # for digit in digits:
    #     sum += int(digit) ** power
    # return sum == n



n = int(input("enter a number: "))

if amg(n):
    print("This is a Armstrong Number ",n)
else:
    print("No Armstrong ",n)    