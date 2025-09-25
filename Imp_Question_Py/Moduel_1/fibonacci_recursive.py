
def fibo(n):

    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input("enter a number: "))

for i in range(n): 
    print(fibo(i))



'''
 fibo(0) = 0
 fibo(1) = 1

fibo(2) = fibo(0) + fibo(1) = 0 + 1 = 1
fibo(3) = fibo(1) + fibo(2) = 1 + 1 = 2
fibo(4) = fibo(2) + fibo(3) = 1 + 2 = 3
fibo(5) = fibo(3) + fibo(4) = 2 + 3 = 5

'''    