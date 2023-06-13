name = input("whats your name?")
''''
if name == "Harry" or name == "Ron":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor)
else:
    print("who?")
'''
#match

match name:
    case " Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case " Draco":
        print("Slytherin")
    case _:
        print("who?")