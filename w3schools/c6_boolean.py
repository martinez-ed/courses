# When you compare two values, the expression is evaluated and Python returns the Boolean value True or False.

print(10 > 9)

# Run a conditional statement:
a = 200
b = 33
if a > b:
  print('a is greater than b')
else:
  print('b is greater than a')

# Evaluate values and variables:
# The bool() function allows you to evaluate any value, and returns True or False.
print(bool('Hello'))
print(bool(15))
print(bool(0))

# Values are False:
print(bool(''))
print(bool(0))
print(bool(()))
print(bool([]))
print(bool({}))
print(bool(False))
print(bool(None))

# Functions can return a Boolean value:
def myFunction():
  return True

if myFunction():
  print('The function returned True')
else:
  print('The function returned False')

# Built-in functions "isinstance" return a boolean value:
x = 200
print(isinstance(x, int))