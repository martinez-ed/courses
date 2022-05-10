# A "Lambda" is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# Syntax:
# lambda arguments : expression
x = lambda a : a + 10
print(x(5)) # 15


# Lambda functions can have any number of arguments:
x = lambda a, b, : a * b
print(x(5, 6))

# E.g. Summarize argument a, b, c and d:
x = lambda a, b, c, d : a + b + c + d
print(x(5, 6, 7, 8)) # 42
print('\n')

# E.g. Use the lambda function to make a function that always doubles the number you send in:
def myfunc(n):
  return lambda a : a * n

doubler = myfunc(2)
print(doubler(11)) # 22

tripler = myfunc(3)
print(tripler(11)) # 33
