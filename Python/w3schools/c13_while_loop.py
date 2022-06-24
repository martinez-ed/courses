# The "while loop" execute a set of statements as long as a condition is true.

# E.g. Print i as long as i is less than 6.
i = 1
while i < 6:
  print(i)
  i += 1

# The "break" statement ends the loop.
i = 1
while i < 6:
  print(i)
  if i == 3:
    break # Stop the loop even if the while condition is true.
  i += 1

# The "continue" statement skips the rest of the current iteration.
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue # Skip the rest of the current iteration.
  print(i, end=' ')
print('\n')

# The "else" clause is executed when the condition is false.
i = 1
while i < 6:
  print(i, end=' ')
  i += 1
else:
  print("i is no longer less than 6")