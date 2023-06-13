'''''
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")

######

while True:
    try:
        x = int(input("What's x? "))
        # we can use break here as well
    except ValueError:
        print("x is not an integer")
#    else:
#        print(f"x is {x}")
    else:
        break #if we use break above we dont need this

print(f"x is {x}")

'''''
#using Function

def main():
    x = get_int("what's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            # we can use break here as well Or,
            # return int(input("what's x? "))
        except ValueError:
            pass
            #print("x is not an integer")
            #pass- wont say anything ignore
    #    else:
    #        print(f"x is {x}")
        else:
            return x #if we use break above we dont need this
    
main()