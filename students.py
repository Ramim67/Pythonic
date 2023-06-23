
'''''
with open("students.csv") as file:
    for line in sorted(file):
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")

#Alternative
import csv
students = []

with open("students.csv") as file:
    for line in sorted(file):
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in sorted(students, key=lambda student:student["name"]):
    print(f"{student['name']} is in {student['house']} ")

##
import csv
students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home":home})

for student in sorted(students, key=lambda student:student["name"]):
    print(f"{student['name']} is in {student['home']} ")

##
#Even if csv columns are interchanged DictReader helps us
import csv
students = []

with open("students.csv") as file:
    reader = csv.DictReader(file) #adding the top row(name,home)
    for row in reader:
        students.append({"name": row["name"], "home":row["home"]})

#Lambda helps creating anonymous function

for student in sorted(students, key=lambda student:student["name"]):
    print(f"{student['name']} is in {student['home']} ")

'''
#writing a CSV
#using DictWriter more useful for writing data
#USed newline='' as it was writing data
#skipping one line in between inside CSV

import csv

name = input("what's your name? ")
home = input("where's your home? ")

with open('students.csv', 'a', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"home": home, "name": name})

