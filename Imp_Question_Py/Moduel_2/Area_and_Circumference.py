
import math

def area_Circumference(r):

    area = math.pi * r * r
    cir =  2 * math.pi * r 

    return area,cir

a,c = area_Circumference(5)
print(f"area : {a}, circumference {c}")