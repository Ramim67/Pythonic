import math
import cmath
#String_Methods

name = input("What is your name? ").strip().title()

first, last = name.split(" ")
# name = name.capitalize()
print(f"Hello, {first} {last}") #format string
print("Hello, \"Ramim\"") #quotation
print("Hello " + name) #Concatanation
print("Hello,", name) #simple variable
print("Hello", {name})

#INTEGER
#tooo = ''
def main(to):
    x = int(input("whats x?"))
    print(f"{x} sqaure is, {square(x)}")
    hello(name, to)
def square(n):
    return n*n

def hello(t,to):
    print(f"Hello, {t} , You are {to}!")

main(to='correct')




