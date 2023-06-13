'''''
##List

students = ["Harry", "Hermione", "Ron"]

for student in students:
    print(student)

for i in range(len(students)):
    print(i+1, students[i])

#DICTIONARY

students = {
    "Hermione": "Gryffindor",
    "Harry"   : "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
    }

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

for student in students:
    print(student, students[student], sep=', ')

###
'''''
students = [
    {"name": "Hermione", "house":"Gryffindor", "patronus" : "otter"},
    {"name": "Harry", "house":"Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}

]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=', ' )





