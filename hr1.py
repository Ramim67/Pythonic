if __name__ == '__main__':
    n = int(input())

i=1

if n >= 1 and n <= 150:
    while i <= n:
        print(i, end="")
        i += 1
    else:
        pass

else:
    print("Out of range")