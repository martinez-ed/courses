# Built-in Math Functions

# The "min()" and "max()" functions can be used to find the lowest and highest values in a iterable:
x = min(5, 10, 15, 20, 25)
y = max(5, 10, 15, 20, 25)
print(x, y) # 5 25

# The "abs()" function returns the absolute (positive) value of a number:
x = abs(-7.25)
print(x) # 7.25

# The "pow(x, y)" function returns x to the power of y:
x = pow(4, 3)
print(x) # 4^3 = 64

# The "round(x, n)" function returns x rounded to n decimal places:
x = round(3.75, 1)
print(x) # 3.8


## The "math" module
# To use it, import the "math" module:
import math

# The "sqrt()" function returns the square root of x:
x = math.sqrt(64)
print(x) # 8.0

# The "math.ceil()" method rounds a number upwards to its nearest integer; and the "math.floor()" method rounds a number downwards to its nearest integer:
x = math.ceil(3.75) # 4
y = math.floor(3.75) # 3
print(x, y)

# The "math.factorial()" method returns the factorial of a number:
x = math.factorial(5) # 120
print(x)

# The "math.gcd()" method returns the greatest common divisor of two numbers:
x = math.gcd(12, 16) # 4
print(x)

# The "math.log()" method returns the natural logarithm of x:
x = math.log(64) # 2.0
print(x)

# The "math.modf()" method returns the fractional and integer parts of x:
x = math.modf(3.75) # (0.75, 3.0)
print(x)

# The "math.pi" constant returns the value of pi:
x = math.pi # 3.141592653589793
print(x)