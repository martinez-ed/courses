# A "for" loop is used to iterate over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# Syntax:
# for variable in sequence:
#     # do something with variable

fruits = ["apple", "banana", "cherry"] # list
for i in fruits:
  print(i)

# Loop through the letters in the word "banana" in the list "fruits":
for i in fruits[1]:
  print(i, end="_")
print('\n')
# The "break" statement can be used to "break" out of a loop.

# The "continue" statement can be used to "continue" to the next iteration of the loop.


# The "range()" function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for i in range(10):
  print(i, end=" ")
print('\n')

# Using the start parameter:
for i in range(5, 10):
  print(i, end=" ") # 5 6 7 8 9
print('\n')

# Adding the step parameter:
for i in range(0, 10, 2):
  print(i, end=" ") # 0 2 4 6 8
print('\n')


# "Else" in a for loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished.
for i in range(6):
  print(i, end=" ") # 0 1 2 3 4 5
else:
  print("Finally finished!")
print('\n')

# E.g. Break the loop when i is 3:
for i in range(6):
  if i == 3: break
  print(i, end=" ") # 0 1 2
else:
  print("Finally finished!")
print('\n')


# Nested loops
cars = ["Ford", "Volvo", "BMW"]
names = ["John", "Paul", "George", "Ringo"]

for i in cars:
  for j in names:
    print(i, j) # Ford John, Ford Paul, Ford George, Ford Ringo, Volvo John, ...
print('\n')


# The pass Statement
# The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action.