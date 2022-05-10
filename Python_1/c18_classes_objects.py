# Python Classes/Objects
# Almost everything in Python is an object.
# A Class is like an object constructor, or a "blueprint" for creating objects.

# Syntax:
# class ClassName:
#   <statement-1>
#   .
#   .
#   .
#   <statement-N>


## Create a class named MyClass, with a property named 'val'
print("\nCreate a class named MyClass, with a property named 'val'")
class MyClass:
  val = 5
print(MyClass) # <class '__main__.MyClass'>
print(MyClass.val) # 5


## Create Object
# Create an object named my_obj from the class MyClass
print("\nCreate Object from Class 'MyClass'")
my_obj = MyClass()
print(my_obj) # <__main__.MyClass object at 0x7f8b8b8b9c10>
print(my_obj.val) # 5


## The __init__() Function
# The init() function is called automatically every time the class is being used to create a new object.
print('\nThe __init__() Function:')

class Person:
  def __init__(self, name, age):
    self.name = name # self.name is an attribute of the class Person
    self.age = age # self.age is an attribute of the class Person

p1 = Person('John', 36)
print(p1.name) # John
print(p1.age) # 36


## Object Methods
# Methods are functions defined inside the class.
print('\nObject Methods:')

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myFunc(self):
    print('Hello my name is ' + self.name)

p1 = Person('John', 36)
p1.myFunc() # Hello my name is John


## The self Parameter
# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
print('\nThe self Parameter:')

class Person:
  def __init__(mySillyObj, name, age):
    mySillyObj.name = name
    mySillyObj.age = age

  def myFunc(abc):
    print('Hello my name is ' + abc.name)

p1 = Person('John', 36)
p1.myFunc() # Hello my name is John


## Modify Object Properties
# Modify the value of an object property
print('\nModify Object Properties:')
p1.age = 40
print(p1.age) # 40