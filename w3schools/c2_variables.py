# Creating variables
x = 5
x = 6.4
y = "Hello, World!"
print(x,y)

# Casting
x = str(5) # x will be '5'
y = int(2.8) # y will be 2
z = float("3") # z will be 3.0
print(x,y,z)

# Get the type of a variable
print(type(x))
print(type(y))
print(type(z))

# Case sensitivity
a = 5
A = 'Hello'
print(a == A)

# Variable names
myvar = "Hello"
my_var = "Hello"
_my_var = "Hello"
myVar = "Hello"
MYVAR = "Hello"
myVar2 = "Hello"

# CamelCase
# Each word, except the first, starts with a capital letter:
myVariableName = "Hello"

# PascalCase
# Each word starts with a capital letter:
MyVariableName = "Hello"

# SnakeCase
# Each word is separated by an underscore:
my_variable_name = "Hello"

# Many values to Multiple Variables:
x, y, z = "Orange", "Banana", "Cherry"
print(x,y,z)

# One value to Multiple Variables:
x = y = z = "Orange"
print(x, y, z)

# Unpack a collection into multiple variables:
fruits = ["Orange", "Banana", "Cherry"]
x, y, z = fruits
print(x, y, z)

# Output variables:
x = 'Python is awesome'
print(x)

x = 'Python'
y = 'is'
z = 'great'
print(x, y, z)

x = 'Python'
y = 'is'
z = 'fun'
print(x + ' ' + y + ' ' + z)

x = 5 
y = 10
print(x + y)

x = 5
y = 'John'
print(x, y)

# Global variables:
x = 'all awesome'
def myfunc():
  print('Python is ' + x)
myfunc()

## Global variables inside functions:
def myfunc():
  global x
  x = 'all great'
myfunc()
print('Python is ' + x)
