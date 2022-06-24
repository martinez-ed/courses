#   if condition:
#       statement(s)
#   elif condition:
#       statement(s)
#   else:
#       statement(s)

a = int(input("Enter a number: "))
if a > 0:
  print("Positive number")
elif a < 0:
  print("Negative number")
else:
  print("Zero")

# Short hand if:
# If you have only one statement to execute, you can put it on the same line as the if statement.
if a > 0: print("Positive number")

# Short hand if...else:
# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line.
# a = 2
b = 330
print('A') if a > b else print('B') # Ternary operator

# Multiple else statements on the same line:
print('A') if a > b else print('=' if a == b else 'B')


# "AND" operator used to combine conditional statements:
a = 200; b = 33; c = 500
if a > b and c > a:
  print("Both conditions are True")


# "OR" operator used to combine conditional statements:
a = 200; b = 33; c = 500
if a > b or a > c:
  print("At least one of the conditions is True")


# "Nested if" statement:
x = 41
if x > 10:
  print('Above ten,')
  if x > 20:
    print('and also above 20!')
  else:
    print('but not above 20.')


# The pass statement:
# The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute.
if a > b:
  pass