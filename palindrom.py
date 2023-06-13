""" #in this code we will write a code for palindrom using while loop

# Python program to check if number is Palindrome

# take inputs
num = int(input('Enter the number: '))

# calculate reverse of number
reverse = 0
number = num
while(num != 0):
  remainder = num % 10
  reverse = reverse * 10 + remainder
  num = int(num / 10)

# compare reverse to original number
if(number == reverse):
  print(number,'is a Palindrome')
else:
  print(number,'is not a Palindrome') """

""" # Python program to check if number is Palindrome using recursion

reverse, base = 0, 1
def findReverse(n):
    global reverse  #function definition
    global base   #function definition
    if(n > 0):
        findReverse((int)(n/10))
        reverse += (n % 10) * base
        base *= 10
    return reverse

# take inputs
num = int(input('Enter the number: '))

# calling function and display result
reverse = findReverse(num)
if(num == reverse):
  print(num,'is a Palindrome')
else:
  print(num,'is not a Palindrome')
 """

#check if it is palindrom using string slicing

num = input('Enter something: ')

rev = (num)[::-1] # string slicing [start:stop:step]

if (num ==  rev):
    print('Palindrom')
else:
    print('Not Palindrom')


#simpler version

#num = input('Enter a number: ')

#if (num == num[::-1]):
#    print(num,'Is Palindrom')
#else:
#   print(num,'Is Not Palindrom') 
    
