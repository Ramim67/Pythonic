# in this program we will calculate the area of
# a triangle
import math
import cmath


x, y, z = input("Enter three values: ").split()
print("first side: ", x)
print("second side:", y)
print("third side: ", z)

a = int(x) ; b= int(y)  ;c=int(z)

print(type(x))
print(type(a))

s = float((a + b + c)/2)

#print(s)

area = math.sqrt(s*(s-a)*(s-b)*(s-c))

#area = (s*(s-x)*(s-y)*(s-z)) ** 0.5

print('area is %0.3f '%area)

print('area is ', area)

print('area is %d '%area)


