"""
Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: 
Consider use range(#begin, #end) method"""
"""
l = []

for n in range(2000, 3201):
    if n % 7 == 0 and n % 5 != 0:
        l.append(str(n))

print(','.join(l))
"""
"""
Question-2: Write a program which can compute the factorial of a given 
numbers. The results should be printed in a comma-separated sequence 
on a single line. Suppose the following input is supplied to the 
program: 8 Then, the output should be: 40320

Hints: In case of input data being supplied to the question, 
it should be assumed to be a console input."""
"""
def fact(x):
    if x == 0:
        return 1 
    return x * fact(x - 1)

x=int(input("Enter a number: "))
print(fact(x))
"""
"""
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
"""
"""
Question-3: With a given integral number n, write a program to generate
 a dictionary that contains (i, i*i) such that is an integral number 
 between 1 and n (both included). and then the program should print
  the dictionary. Suppose the following input is supplied to the 
  program: 8 Then, the output 
  should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Hints: In case of input data being supplied to the question, 
it should be assumed to be a console input. Consider use dict()
"""
"""
l = dict()

n = int(input("Enter a number: "))

for i in range(1, n+1):
    l[i] = i*i

print(l)
"""
"""
Question 4

Level 1

Question: Write a program which accepts a sequence of comma-separated 
numbers from console and generate a list and a tuple which contains 
every number. Suppose the following input is supplied to the 
program: 34,67,55,33,12,98 Then, the output 
should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')

Hints: In case of input data being supplied to the question, 
it should be assumed to be a console 
input. tuple() method can convert list to tuple

"""
"""
x = input().split(",")
y = tuple(x)

print(x, end="")
print(y)
"""
"""
Question 5

Level 1

Question: Define a class which has at least two methods: getString: to
 get a string from console input printString: to print the 
 string in upper case. Also please include simple test function 
 to test the class methods.

Hints: Use init method to construct some parameters
"""
"""
class Stringy:
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("whats String?")
    
        #return s
    def printString(self):
        print(self.s.upper())

def main():

    get_string = Stringy()
    get_string.getString()
    get_string.printString()

main()
"""
#if "__name__" == "__main__":
#    main()

"""
Question 6

Level 2

Question: Write a program that calculates and prints the value
according to the given formula: Q = Square root of [(2 * C * D)/H] 
Following are the fixed values of C and H: C is 50. H is 30. D is
the variable whose values should be input to your program in 
a comma-separated sequence. Example Let us assume the following 
comma separated input sequence is given to the 
program: 100,150,180 The output of the program should be: 18,22,24

Hints: If the output received is in decimal form, it should be 
rounded off to its nearest value (for example, if the output
                                   received is 26.0, it should be 
                                   printed as 26) In case of input 
data being supplied to the question, it should be assumed to be a 
console input."""

"""
import math

C = 50
H = 30
value = [x for x in input("Enter: ").split(",")]
Q= []
#Q = math.sqrt[(2*C*D)/H]

for D in value:

    Q.append(str(int(round(math.sqrt((2*C*float(D))/H)))))



print(",".join(Q))
"""
"""
Question 7

Level 2

Question: Write a program which takes 2 digits, X,Y as input and 
generates a 2-dimensional array. The element value in the i-th row and
j-th column of the array should be i*j. 
Note: i=0,1.., X-1; j=0,1,¡­Y-1. Example Suppose the following inputs 
are given to the program: 3,5 Then, the output of the program should 
be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

Hints: Note: In case of input data being supplied to the question, 
it should be assumed to be a console input in a comma-separated form.
"""
"""
input_str = input()
dimensions=[int(x) for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col

print(multilist)
"""
"""
Question 8

Level 2

Question: Write a program that accepts a comma separated 
sequence of words as input and prints the 
words in a comma-separated sequence after sorting them alphabetically. 
Suppose the following input is supplied to the 
program: without,hello,bag,world Then, the output should 
be: bag,hello,without,world

Hints: In case of input data being supplied to the question, 
it should be assumed to be a console input.
"""
"""
l = list(input("Enter item: ").split(","))

print(sorted(l))
"""
"""
items=[x for x in input().split(',')]
print(items.sort())
print(','.join(items))
"""
"""
Question 9

Level 2

Question£º Write a program that accepts sequence 
of lines as input and prints the lines after 
making all characters in the sentence capitalized.
Suppose the following input is supplied to the 
program: Hello world Practice makes perfect Then,
the output should be: HELLO WORLD PRACTICE MAKES 
PERFECT

Hints: In case of input data being supplied to 
the question, it should be assumed to be a console
input."""


#items = [x for x in input().upper().split(',')]

#print(items)
"""
lines = []
while True:
    s = input()
    if s:
        lines.append(s.upper())
    else:
        break;

for sentence in lines:
    print(sentence)
"""
"""
Question 10

Level 2

Question: Write a program that accepts a sequence
of whitespace separated words as input and prints
the words after removing all duplicate words and
sorting them alphanumerically. Suppose the 
following input is supplied to the 
program: hello world and practice makes perfect 
and hello world again Then, the output should 
be: again and hello makes perfect practice world

Hints: In case of input data being supplied to 
the question, it should be assumed to be a console
input. We use set container to remove duplicated 
data automatically and then use sorted() to sort 
the data."""
"""
l = set(input().split(" "))

for i in sorted(l):
    print(i, end=" ")
"""
##
s = input()
words = [word for word in s.split(" ")]
print(" ".join(sorted(list(set(words)))))

####### ------------------ #######