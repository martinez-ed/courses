# Tuples are used to store multiple items in a single variable.
# Tuples are immutable, meaning that they cannot be changed.
# Tuple items are ordered, unchangeable, and allow duplicate values.

# Create a tuple:
myTuple = ('apple', 'banana', 'cherry')
print(myTuple)

# Allow Duplicates:
myTuple = ('apple', 'banana', 'cherry', 'apple')
print(myTuple)

# Tuple Length:
print(len(myTuple))

# Tuple with one item: 
# (You have to put a comma after the last item)
oneTuple = ('apple',)
print('Tuple with one item: ', oneTuple)

# Tuple Items - Data Types:
# E.g., String, int and boolean data types:
tuple1 = ('apple', 'banana', 'cherry')
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, True, True)
print(tuple1, tuple2, tuple3)

# A tuple can contain different data types:
myTuple = ('abc', 34, True, 'xyz')
print(myTuple)

# type() function:
print(type(myTuple))

# The tuple() Constructor:
newTuple = tuple(('apple', 'banana', 'cherry')) # note the double parentheses
print(type(newTuple), newTuple)

# ACCESS TUPLES
# Accessing Values in a Tuple:
myTuple = ('apple', 'banana', 'cherry')
print(myTuple[1])
print(myTuple[-1])
print(myTuple[0:2])

# Check if Item Exists:
if 'apple' in myTuple:
  print('Yes, "apple" is in the fruits tuple')


# UPDATE TUPLES
# Tuples are immutable, so you cannot change a tuple.

# Convert the tuple into a list to be able to change it:
t = ('a', 'b', 'c', 'd')
print('Initial tuple: ',t)
x = list(t)
x[1] = 'new'
t = tuple(x)
print('Change item: ',t)

# Add Items to a Tuple:
x = list(t)
x.append('new2')
t = tuple(x)
print('Add item: ',t)

# Add tuple to a tuple:
thisTuple = ('apple', 'banana', 'cherry')
y = ('orange',) # note the comma
thisTuple += y
print(thisTuple)

# Remove Items from a Tuple:
# Convert the tuple into a list to be able to change it:
t = ('a', 'b', 'c', 'd')
print('Initial tuple: ',t)
x = list(t)
x.remove('b')
t = tuple(x)
print('Remove item: ',t)

# Delete the tuple completely:
del thisTuple
# print(thisTuple) # this will cause an error


# UNPACK TUPLES

fruits = ('apple', 'banana', 'cherry')
print(fruits)

(x, y, z) = fruits
print('Unpacking a tuple: ', x, y, z) # note the order

# Using Asterisk *:
names = ('John', 'Paul', 'George', 'Ringo', 'Emma', 'Sophia')
print(names)

(x, y, z, *name) = names # Assign the rest of the values as a list called "name"
print('Unpacking a tuple: ', x, y, z, name) # note the order

# Asterisk added to another variable name than the last item in the tuple:
(x, y, z, *name, last) = names
print('Unpacking added than the last: ', x, y, z, name, last)


# LOOP TUPLES
myTuple = ('apple', 'banana', 'cherry')

# Loop through a tuple:
for i in myTuple:
  print(i)

# Loop through a tuple with index:
for i in range(len(myTuple)):
  print(myTuple[i] + ' is at index ' + str(i))

# Using a while loop:
i = 0
while i < len(myTuple):
  print(myTuple[i])
  i += 1


# JOIN TUPLES
# Use the + operator to join two tuples:
tuple1 = ('a', 'b', 'c')
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply a tuple:
fruits = ('apple', 'banana', 'cherry')
t = fruits * 2
print(t)


# TUPLE METHODS
myTuple = ('a', 'b', 'c', 'd', 'a', 'b', 'z', 'd', 'a', 'b', 'c', 'd')
print(myTuple)

# count()
# Return the number of times a specified value occurs in a tuple:
print('Number of occurs the value "a": ', myTuple.count('a'))

# index()
# Search and return the position of where it was found:
t = myTuple.index('z')
print('The index of "z" is: ', t)