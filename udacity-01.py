"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""

class MyClass:
    def __init__(self):
        self.my_list = []

    def add_to_list(self, argument):
        self.my_list.append(argument)

    def process_list(self):
        # Call another function and pass the list as an argument
        self.another_function(self.my_list)

    def another_function(self, some_list):
        # Perform operations on the received list
        total = 0
        for item in some_list:
            
            if item == "tophat":
                total += 2
            elif item == "bowtie":
                total += 4
            elif item == "monocle":
                total += 5
            else :
                total += 0
                
        print(total)

# Create an instance of the class
my_instance = MyClass()

my_instance.process_list()
# Call the method and pass the argument
my_instance.add_to_list("bowtie")
my_instance.add_to_list("tophat")

# Call the method that processes the list
my_instance.process_list()
my_instance.add_to_list("monocle")

my_instance.process_list()

    
'''
class Classy:
    def __init__(self):
        self.items = []
#        self.house = house

#    def __str__(self):
#        return f"{self.item}"
    
    
    def addItem(self, n):
        self.items.append(n)
#        return (items)

    def process_list(self):
        # Call another function and pass the list as an argument
        self.getClassiness(self.items)

    def getClassiness(self, list):
        
        total = 0
        for item in list:
            if item == "tophat":
                total += 2
            elif item == "bowtie":
                total += 4
            elif item == "monocle":
                total += 5
            else :
                total += 0
                
        return total
    
#def main():
    #classy = Classy.addItem()
#    classiness = Classy.getClassiness()
    #print(classy)
#    print(classiness)

# Create an instance of the class
me = Classy()
# Call the method and pass the argument
print(me.addItem("Bowtie"))

print(me.process_list())

'''




#if __name__ == "__main__":
#    main()


"""
    def getClassiness():
        
        total = 0
        for item in self.items:
            if item == "tophat":
                total += 2
            elif item == "bowtie":
                total += 4
            elif item == "monocle":
                total += 5
            else:
                total += 0
                
        return total
        
# Test cases
me = Classy()

# Should be 0
print(me.getClassiness())

me.addItem("tophat")
# Should be 2
print(me.getClassiness())
me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print(me.getClassiness())

me.addItem("bowtie")
# Should be 15
print(me.getClassiness())

"""