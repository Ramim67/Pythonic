x = int(input("what's x ?"))

if x % 2 == 0:
    print("Even")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def is_even(n):
    #return True if n % 2 == 0 else False
#or,
    return n % 2 == 0
