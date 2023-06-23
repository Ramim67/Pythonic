def main():
    yell("This", "is", "CS50")

def yell(*words):
#    uppercased= map(str.upper, words)
    uppercased = [word.upper() for word in words]
#    for word in words:
#        uppercased.append(word.upper())
    print(*uppercased)

if __name__ == "__main__":
    main()