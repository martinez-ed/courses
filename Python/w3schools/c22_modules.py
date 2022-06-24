# Considere a module to be the same as a code library.

## Importing a module
# Inport the module named "c22_module_demo1" and call the greeting function:
import c22_module_demo1

print('\nCall the greeting function:')
c22_module_demo1.greeting('Michael')


## Variables in Modules
# Import the module named "c220_module_demo2", and access the person1 dictionary:

# import c22_module_demo2

# a = c22_module_demo2.person1['age']
# print('\nPrint the age:')
# print(a)


## Re-naming a module
# Use the "as" keyword to rename the module:
import c22_module_demo2 as mx

a = mx.person1['age'] # Access the age
print('\nPrint the age:')
print(a)


## Built-in Modules
# Are several modules that come with Python.
# The "sys" module provides access to the system modules.
# The "os" module provides access to the operating system modules.
# The "math" module provides access to the mathematical functions.
# The "random" module provides access to the random functions.
# The "time" module provides access to the time functions.
# The "datetime" module provides access to the datetime functions.
# The "collections" module provides access to the collections functions.
# The "re" module provides access to the regular expression functions.
# The "csv" module provides access to the csv functions.
# The "json" module provides access to the json functions.
# The "pickle" module provides access to the pickle functions.
# The "urllib" module provides access to the urllib functions.
# The "xml" module provides access to the xml functions.
# The "html" module provides access to the html functions.
# The "http" module provides access to the http functions.
# The "socketserver" module provides access to the socketserver functions.
# The "subprocess" module provides access to the subprocess functions.
# The "base64" module provides access to the base64 functions.
# The "hashlib" module provides access to the hashlib functions.
# The "email" module provides access to the email functions.
# The "ftplib" module provides access to the ftplib functions.
# The "smtplib" module provides access to the smtplib functions.
# The "sqlite3" module provides access to the sqlite3 functions.


## Import From a Module
# The module named "c22_module_demo3" has one function and one dictionary.
# Import only the "person1" dictionary:
from c22_module_demo3 import person1

print('\nPrint the address:')
print(person1['address'])