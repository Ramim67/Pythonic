# a program to solve quadratic equations

import cmath

x, y, z = input('Enter the variables:').split()

a = int (x) ; b = int(y) ; c = int(z)

# we need to define discriminant "d"

d = b**2 - 4*a*c

#two possible solutions
s1 = (-b + cmath.sqrt(d))/(2*a)
s2 = (-b - cmath.sqrt(d))/(2*a)


print('the solutins are:{0}, {1}'.format(s1 , s2))

