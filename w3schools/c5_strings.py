# Assign String to a Variable:
a = 'Hello World'
print('1)', a) 

# Multiline Strings:
b = """This is a multiline string.
It can span multiple lines."""
print('2)', b) 

# Strings are arrays of bytes:
c = 'Hello, World!'
print(c[1])
print(c[2:5])

# looping through strings:
for x in 'Hello, World!':
    print(x, end='-')

# String Length:
a = 'Hello, World!'
print(len(a))

# Check String:
txt = 'The best things in life are free!'
x = 'life' in txt
print(x)

txt = 'The beautiful life is awesome!'
if 'beautiful' in txt:
  print('Yes, [beautiful] is in the text!')

# Check if NOT in String:
txt = 'The best things in life are free!'
print('freedom' not in txt)

if 'expensive' not in txt:
  print('No, [expensive] is not in the text!')

# Slicing Strings:
b = 'Hello, World!'
print(b[0:4])
print(b[4:]) # from index 2 to the end
print(b[-5:-2]) # Start from the end and go backwards

# Upper and Lower Case:
a = 'Hello, World!'
print(a.upper())
print(a.lower())

# Remove Whitespace:
a = ' Hello, World! '
print(a.strip()) # Remove whitespace from both sides
print(a.lstrip()) # Remove whitespace from the left
print(a.rstrip()) # Remove whitespace from the right

# Replace String:
a = 'Hello, World!'
print(a.replace('H', 'J'))

# Split String:
# The split() method splits the string into substrings if it finds instances of the separator:
a = 'Hello, World!'
print(a.split(',')) # returns a list ['Hello', ' World!']

# String Concatenation:
a = 'Hello'
b = 'World'
print(a + ' ' + b)

# String Format:
# The format() method takes the passed arguments, formats them, and places them in the string where the placehoders {} are:
age = 40
txt = 'My name is John, and I am {}'
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = 'I want {} pieces of item {} for {} dollars.'
print(myorder.format(quantity, itemno, price))

myorder2 = 'I want to pay {2} dollars for {0} pieces of item {1}.'
print(myorder2.format(quantity, itemno, price))

# Escape Character:
txt = 'We are the so-called \"Vikings\" from the north.'
print(txt)

# STRING METHODS:

# capitalize() - Converts the first character to upper case
txt = 'hello, and welcome to my world.'
print(txt.capitalize())

# casefold() - Converts string into lower case
txt = 'Hello, And Welcome To My World.'
print(txt.casefold())

# center() - Returns a space-padded string with the original string centered
txt = 'Hello, World!'
print(txt.center(50, '*'))

# count() - Returns the number of times a specified value occurs in a string
txt = 'I love apples, apples are my favorite fruit.'
print(txt.count('apple'))

# encode() - Returns an encoded version of the string
txt = 'My name is Martínez Ed'
print(txt.encode())

# endswith() - Returns true if the string ends with the specified value
txt = 'Hello, welcome to my world.'
print(txt.endswith('world.'))

# expandtabs() - Expands tab characters into spaces
txt = 'H\te\tl\tl\to'
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

# find() - Searches the string for a specified value and returns the position of where it was found
txt = 'Hello, welcome to my world.'
print(txt.find('welcome'))

# format() - Formats specified values in a string
txt = 'For only {price:.2f} dollars!'
print(txt.format(price = 49))

# isalnum() - Returns True if all characters in the string are alphanumeric
txt = 'Hello123'
print(txt.isalnum())

# isalpha() - Returns True if all characters in the string are in the alphabet
txt = 'Company10' # False
print(txt.isalpha())

# isdigit() - Returns True if all characters in the string are digits
txt = '12345'
print(txt.isdigit())

# join() - Converts the elements of an iterable into a string
mytuple = ('John', 'Peter', 'Vicky')
print(', '.join(mytuple))

myDict = {'name': 'John', 'age': '35', 'city': 'New York'}
mySeparator = ', '
print(mySeparator.join(myDict))

# ljust() - Returns a left justified version of the string
txt = 'banana'
print(txt.ljust(30, '.'))

# lstrip() - Returns a left trim version of the string
txt = ',,,,,,ssaww....banana'
print(txt.lstrip(',.asw'))

# partition() - Splits the string at the specified separator and returns a tuple
txt = 'edeyeme@gmail.com'
print(txt.partition('@'))
print(txt.partition('@')[2])

# rjust() - Returns a right justified version of the string
txt = 'banana'
print('3', txt.rjust(30, '.'))

# zfill() - Fills the string with a specified number of 0 values at the beginning
a = 'hello'
b = 'welcome to the jungle'
c = '10.000'
print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))