
import math 

def cal(radius):
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    return (area, circumference)  # return tuple


radius = float(input("enter a radius of circle "))

area ,circumference = cal(radius)

print("Area ",area)
print("Circumference ",circumference)