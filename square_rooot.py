'''
# python program to calculate the square root

num = float(input('Enter a number: '))
num_sqrt = num ** 0.5
print ('The square root of %0.3f is %0.3f'%(num ,num_sqrt))

'''
#square root of a imaginary number 

import cmath

#num = 1+2j
num = eval(input('Enter a number: '))
square_root = cmath.sqrt(num)

print('The square root 0f {0} is {1:0.3f}+{2:0.3f}j'.format(num, square_root.real, square_root.imag))



