# There are three numeric types in Python:
# int, float, complex.
x = 1 # int
y = 2.8 # float
z = 1j # complex
print(type(x), type(y), type(z))

# Integer
x = 1
y = 35656222554887711
z = -3255522
print(type(x), type(y), type(z))

# Float
x = 1.10  # decimal number
y = 35e3 # scientific notation
z = -87.7e100 # also scientific notation
print(type(x), type(y), type(z))

# Complex
x = 3 + 5j
y = 5j
z = -5j
print(type(x), type(y), type(z))

#Type Conversion:
x = 1 # int
y = 2.8 # float
z = 1j # complex

a = float(x) # convert x to float
b = int(y) # convert y to int
c = complex(x) # convert x to complex
d = str(z) # convert x to string

print(a, b, c, d)

# Random Numbers:
import random # import the random module
print(random.randrange(1,10)) # random integer between 1 and 10