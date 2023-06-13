import sys

print("Hello, My name is", sys.argv[1] )

print("Hello, My name is " + sys.argv[1] )

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print('Too many arguments')
else:
    print("Hello, My name is ", sys.argv[1])


