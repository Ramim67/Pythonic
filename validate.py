'''''
email = input("What's your email? ").strip()

username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")

'''
##Better version
# [^@] any character but @
# + means 1 or more repetations of chracter
#^ --- $ start and end of matching sequence
#r"" for regular expressions
# \w means [a-zA-Z0-9_]
#\s means white space
# [^@] anything except @

import re

email = input("what's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.(com|edu|net|gov|org)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

