'''
names = []

for _ in range(3):
    names.append(input("what's your name? "))

for name in sorted(names):
    print(f"hello, {name}")



name = input("what's your name? ")

#file = open("names.txt", "a") #a for append

with open("names.txt", "a") as file:
    file.write(f"{name}\n")

#file.close() -no need when used open

#Reading

with open("names.txt", "r") as file:
    lines = file.readlines()
for line in lines:
    print("hello, line")

    
names = []

for _ in range(3):

    name = input("What's your name? ")

    with open("names.txt", "a") as file:
        file.write(f"{name}\n")


##REading
names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
for name in sorted(names):
    print(f"hello, {name}")
'''''

#Default its reverse=False since it's sorted

names = []
with open("names.txt") as file:
    for line in sorted(file, reverse=True): 
        print("hello,", line.rstrip())







