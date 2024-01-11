"""
Question 11

Level 2

Question: Write a program which accepts a sequence of comma separated 
4 digit binary numbers as its input and then check whether they are 
divisible by 5 or not. The numbers that are divisible by 5 are to be 
printed in a comma separated sequence. Example: 0100,0011,1010,1001 
Then the output should be: 1010 Notes: Assume the data is input by
console.

Hints: In case of input data being supplied to the question, it should
be assumed to be a console input.
"""
"""
n = (x for x in input().split(","))
Q = []

for i in n:
    intp = int(i, 2)

    if intp % 5 != 0:
        Q.append(i)


print(",".join(Q))
"""
"""
value = []
items=[x for x in input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)

print(','.join(value))
"""
"""
Question 12

Level 2

Question: Write a program, which will find all such numbers between 
1000 and 3000 (both included) such that each digit of the number is 
an even number. The numbers obtained should be printed in a 
comma-separated sequence on a single line.

Hints: In case of input data being supplied to the question, it should 
be assumed to be a console input."""
"""
values = []
for n in range(1000, 3001):

    s = str(n)

    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)

print(",".join(values))




"""

"""
Question 13

Level 2

Question: Write a program that accepts a sentence and calculate the 
number of letters and digits. Suppose the following input is supplied
to the program: hello world! 123 Then, the output should be: 
LETTERS 10 DIGITS 3

Hints: In case of input data being supplied to the question, it should
be assumed to be a console input."""
"""
s = input()

d = {"DIGITS": 0, "LETTERS":0}

for c in s:
    if c.isdigit():
        d["DIGITS"] += 1
    elif c.isalpha():
        d["LETTERS"] += 1
    else:
        pass

print("LETTERS", d["LETTERS"])
print("DIGITS", d["DIGITS"])

"""
"""
Question 14

Level 2

Question: Write a program that accepts a sentence and calculate the
number of upper case letters and lower case letters. Suppose the 
following input is supplied to the program: Hello world! Then, the
output should be: UPPER CASE 1 LOWER CASE 9

Hints: In case of input data being supplied to the question, it should
be assumed to be a console input."""
"""
s = input()
d = {"UPPER CASE": 0, "LOWER CASE":0}

for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass

print("UPPER CASE", d["UPPER CASE"])
print("LOWER CASE", d["LOWER CASE"])
"""
"""
Question 15

Level 2

Question: Write a program that computes the value of a+aa+aaa+aaaa 
with a given digit as the value of a. Suppose the following input is
 supplied to the program: 9 Then, the output should be: 11106

Hints: In case of input data being supplied to the question, it should
be assumed to be a console input."""

a = int(input("Enter a Number: "))

a = a+ (a*a) + (a*a*a) + (a*a*a*a)

print(a)

