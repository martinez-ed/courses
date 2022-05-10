# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

#Syntax:
# def functionname(parameter1, parameter2):
#    "function_docstring"
#    function_suite
#    return [expression]

def myFunction():
  print("Hello from a function")

myFunction() # call the function

# Arguments
# When you call a function, you pass arguments to it.
# These arguments are values that are assigned to variables within the function.
print('\nArguments:')
def myFunction(fname):
  print(fname + " Refsnes")

myFunction("Emil")
myFunction("Tobias")
myFunction("Linus")


# Parameters or Arguments

# A "parameter" is the variable listed inside the parentheses in the function definition.
# An "argument" is the value that is sent to the function when it's called.
print('\nParameters and Arguments:')
def myFunction(fname, lname): # "fname" and "lname" are parameters
  print(fname + " " + lname)

myFunction("Ed", "Martinez") # "Ed" and "Martinez" are arguments


# Arbitrary Arguments, *args
# If the number of arguments is unknown, add a * before the parameter name:
print('\nArbitrary Arguments, *args:')
def myFunction(*kids):
  print("The youngest child is " + kids[2]) # "kids" is a list

myFunction('Emil', 'Tobias', 'Linus')


# Keyword Arguments
# Send arguments with the key = value syntax.
print('\nKeyword Arguments:')
def myFunction(child3, child2, child1):
  print("The youngest child is " + child2)

myFunction(child1 = 'Emil', child2 = 'Tobias', child3 = 'Linus')


# Arbitrary Keyword Arguments, **kwargs
# If the number of arguments is unknown, add a double ** before the parameter name:
print('\nArbitrary Keyword Arguments, **kwargs:')
def myFunction(**kwargs):
  print('His last name is ' + kwargs['lname'])

myFunction(fname = 'Ed', lname = 'Martinez')


# Default Parameter Values
# If you don't supply an argument when calling the function, the default value is used.
print('\nDefault Parameter Values:')
def myFunction(country = 'Norway'):
  print('I am from ' + country)

myFunction("Sweden")
myFunction("India")
myFunction() # default value


# Passing a List as an Argument
fruits = ['apple', 'banana', 'cherry']
# You can pass a list as an argument by using the list() function.
print('\nPassing a List as an Argument:')
def myFunction(food):
  for i in food:
    print(i, end = ', ')

myFunction(fruits)


# Return Values
# Use the "return" statement:
print('\nReturn Values:')
def myFunction(x):
  return 5 * x

print(myFunction(3))
print(myFunction(5))
print(myFunction(9))


# Recursion
# A function can call itself:
print('\nRecursion:')
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\nRecursion Example Results:")
tri_recursion(6)