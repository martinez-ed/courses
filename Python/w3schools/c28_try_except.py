# The try block will generate an error, because "x" is not defined:

# try:
#   print(x)
# except:
#   print("An exception occurred")

# E.g. Print one message if the try block raises a NameError, and another if the try block raises a TypeError:
# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except TypeError:
#   print("Variable x is not the right type")

# E.g. The "try" block doesn't generate any error:
try:
  print('Hello')
except:
  print('Something went wrong')
else:
  print('Nothing went wrong')


## Finally
# The "finally" block, if specified, will be executed regardless if the "try" block raises an error or not.

# try:
#   print(x)
# except:
#   print("An exception occurred")
# finally:
#   print("The 'try except' is finished")

# Try to open and write to a file that is not writable:
try:
  f = open('demofile.txt')
  try: 
    f.write('Lorum Ipsum')
  except:
    print('Something went wrong when writing to the file')
  finally:
    f.close()
except:
  print('Something went wrong when opening the file')


## Raise an exception
# To throw (or raise) an exception, use the "raise" keyword.
# x = -1
# if x< 0:
#   raise Exception('Sorry, no numbers below zero')

# E.g. Raise a TypeError if x is not an integer:
x = 'Hello'
if not isinstance(x, int):
  raise TypeError('Only integers are allowed')
