#Ask for name as Input
#name = input("What is Your name? ")
#print ("Hello,",name)

def main():
    name = input("what's your name? ")
    print(hello())

def hello(to='world'):
    return f"hello, {to}"


if __name__ == "__main__":
    main()