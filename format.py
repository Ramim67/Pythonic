import re

'''
name = input("whta's your name? ").strip()
if "," in name:
    last, first =name.split(", ")
    name = f"{first} {last}"
print(f"hello, {name}")


'''
# ? -> tolerating the white space before
# := walrus operator

name = input("What's your name? ").strip()
if matches:= re.search(r"^(.+), *(.+)$", name):
#if matches:
    #last, first = matches.groups()
    #name = f"{first} {last}"
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")