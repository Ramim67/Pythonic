
''''
class Student:
    def __init__(self, name, house, patronus):
#        if not name:
#            raise ValueError("Missing Name")
#        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "🦄"
            case "Otter":
                return "🦦"
            case "Jack Russell Terrier":
                return "🎃"
            case _:
                return "🪄"
    
#Getter
    @property
    def name(self):
        return self._name
#Setter
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name
    
    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Slytherin", "Ravenclaw"]:
            raise ValueError("Invalid House!")
        self._house = house
    

def main():
    
    student = get_student()
    #student.house = "Number Four, Privet Drive"
    print("Expecto Patronum!")
    print(student.charm())
    print(student)
    #if student[0] == "padma":
    #    student[1] = "Ravenclaw"
    #name = get_name()
    #house = get_house()
    #if student["name"] == "padma":
    #    student["house"] = "Ravenclaw"
    #print(f"{student['name']} from {student['house']}")
    #print(f"{student.name} from {student.house}")

#def get_name():
   # return input("Name: ")

#def get_house():
   # return input("House: ")

def get_student():
    #student = Student()  #custom data type student
    #student.name = input("Name: ")
    #student.house = input("House: ")
    #return student
   
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
#   try:
    return Student(name, house, patronus)
#   except Value:
#        ...

    #student = {}
    #student["name"] = input("whats name? ")
    #student["house"] = input("whats house?")
    #return student
    #name = input("Name: ")
    #house = input("House: ")
    #return (name, house)


if __name__ == "__main__":
    main()
    
'''
# Improved Version

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()