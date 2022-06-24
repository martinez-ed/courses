## Local Scope
def myFunc():
  x = 300
  print('\nLocal Scope:')
  print('x =', x)

myFunc()

# Function inside a function
def myFunc2():
  x = 300
  def innerFunc(): # innerFunc is a local function
    print('\nInner Function:')
    print('x =', x)
  innerFunc() # call innerFunc

myFunc2()


## Global Scope
x = 300
print('\nGlobal Scope:')

def myFunc3():
  print('x =', x) # global variable

myFunc3()

print('x =', x)


## Naming Variables
x = 300 # global variable
print('\nNaming Variables:')

def myFunc4():
  x = 200 # local variable
  print('x =', x)

myFunc4()

print('x =', x) # global variable


## Global Keyword
# The "global" keyword is used to modify the value of a global variable.
def myFunc():
  global x # global variable
  x = 200

print('\nGlobal Keyword:')
myFunc()
print('x =', x)

# To change the value of a global variable inside a function, use the "global" keyword.