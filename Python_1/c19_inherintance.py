# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# "Parent class" is the class being inherited from. 
# "Child class" is the class that inherits from the "Parent class".

## Create a Parent Class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname #Atribute of the class Person
    self.lastname = lname #Atribute of the class Person

  def printName(self): # Method
    print(self.firstname, self.lastname)

p1 = Person("John", "Doe")
p1.printName() # Prints the name of the person


## Create a Child Class
class Student(Person): # Child class inherits from the parent class Person
  pass # Use when you don't want to add any other properties or methods.

s1 = Student("Mike", "Olsen")
s1.printName() # Prints the name of the student


## Add the __init__() Function
class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.
    Person.__init__(self, fname, lname) # Call the __init__() function of the parent class

s1 = Student('Mike', 'Olsen')
s1.printName()


## Use the super() Function
# By using the "super()" function, you don't have to use the name of the parent element.
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname) # Call the __init__() function of the parent class

s1 = Student('Ed', 'Martinez')
s1.printName()


## Add Properties
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019 # Add a property

s1 = Student('Mike', 'Olsen')
print(s1.graduationyear) # Prints the graduation year

# Add a year parameter to the __init__() function, and pass the correct year when the object is created:
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname) 
    self.graduationyear = year

s1 = Student('Mike', 'Olsen', 2022)
print(s1.graduationyear) # Prints the graduation year


## Add Methods
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self): # Add a method
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

s1 = Student('Ed', 'Martinez', 2022)
s1.welcome() # Prints the welcome message