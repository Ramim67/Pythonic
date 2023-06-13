'''''
#i = 3

#while i != 0:
 #   print("meow")
 #   i = i-1


i = 1

while i <= 3:
    print("meow")
    i = i + 1
Or, i += 1


#FOR Loops

for i in [0, 1, 2]:
    print("meow")

# Better way

for i in range(3):
    print("meow")

# Pythonic
#whatever variable

for _ in range(3):
    print("meow")

#Or,

print("meow\n" * 3, end="")

####

while True:
    n = int(input("whast n?"))
    if n > 0:
        break

for _ in range(n):
    print("meow")
'''''
###

def main():

    number = get_number()
    meow(number)

def get_number():

    while True:
        n = int(input("Whtas n?"))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()




