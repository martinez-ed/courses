## Open File
# Syntax:
# file = open(filename, mode)

# The "open()" function takes two parameters; filename and mode.

# Methods (modes) for opening a file:
# r - Read - (Default). Opens a file for reading, error if the file does not exist
# w - Write - Opens a file for writing, creates the file if it does not exist
# a - Append - Opens a file for appending, creates the file if it does not exist
# x - Create - Creates the specified file, returns an error if the file exists

# Binary or text mode:
# b - Binary - Opens a file in binary mode
# t - Text - Opens a file in text mode (default)

# Open file for reading
f = open('./files/demofile1.txt', 'r')
print(f.read())

# Read only parts of the file:
f = open('./files/demofile1.txt', 'r')
print(f.read(5)) # Prints the first 5 characters
print(f.readline()) # Reads the first line of the file

# Loop through the lines of the file:
f = open('./files/demofile1.txt')

for line in f:
  print(line, end='')


## Close the file
# It is good practice to always close the file after you are done with it.
f.close()


# Write to a file
print('\n\nWrite to a file:')
# Syntax:
# file = open(filename, mode)
# file.write(string)
# file.close()

# Open file for writing (append mode)
f = open('./files/demofile2.txt', 'a') # Open for appending
f.write('Now the file has more content!')
f.close()
#open and read the file after the appending:
f = open('./files/demofile2.txt', 'r')
print(f.read())
f.close()

# Open file for writing (overwrite mode)
f = open('./files/demofile3.txt', 'w') # Open for writing
f.write('Woops! I have deleted the content!')
f.close()
#open and read the file after the writing:
f = open('./files/demofile3.txt', 'r')
print(f.read())
f.close()


## Create a new file
# Use the "open()" methods:
# "x" - Create - Creates the specified file, returns an error if the file exists
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist

# E.g. Create a file called "demofile4.txt"
f = open('./files/demofile4.txt', 'a')
f.write('\nNow the file newly created has more content!')
f.close()
#open and read the file after the writing:
f = open('./files/demofile4.txt', 'r')
print(f.read())
f.close()


## Delete a file
# To delete a file, import the "os" module and use the "os.remove()" function:
# import os

# To avoid getting an error, check if the file exists before deleting it.
# if os.path.exists('./files/demofile4.txt'):
#   os.remove('./files/demofile4.txt')
# else:
#   print('The file does not exist')


## Delete Folder
# To delete a folder, use the "os" module and use the "os.rmdir()" function:
# import os
# os.rmdir('./files')
