# Create a list:
thislist = ["apple", "banana", "cherry"]
print(thislist)

# Access items:
print(thislist[1])

# Negative indexing:
print(thislist[-1])

# Range of indexes:
print(thislist[1:])

# Change values:
thislist[1] = "blackcurrant"
print(thislist)

thislist2 = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thislist2)
thislist2[1:3] = ['blackcurrant', 'watermelon']
print(thislist2)

# List length:
print(len(thislist))

# List Items - Data Types:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, True, True]
list4 = ["apple", "banana", "cherry", 1, 5, 7, 9, 3, True, False, True, True]
print(list4)

# Check if item exists:
if 'apple' in list1:
  print("Yes, 'apple' is in the fruits list")

# ADD LIST ITEMS:
# Using the append() method:
list1.append("orange")
print(list1)

# Insert items:
list1.insert(1, "orange")
print(list1)

# Using the extend() method:
newList = ['mango', 'pineapple', 'papaya']
list1.extend(newList)
print(list1)

# Add elements of a tuple to a list:
tuple1 = ('kiwi', 'orange')
list1.extend(tuple1)
print(list1)

# REMOVE LIST ITEMS:
# The remove() method removes the specified item:
list1.remove('orange')
print(list1)

# The pop() method removes the specified index, (or the last item if index is not specified):
list1.pop(1)
print(list1)

# The del keyword removes the specified index:
del list1[1]
print(list1)

# The clear() method empties the list:
# list1.clear()
# print(list1)

# LOOP LIST:
# Loop through a list:
for i in list1:
  print(i)
print('\n')

# Loop through the Index Numbers:
for i in range((len(list1))):
  print(list1[i])
print('\n')

# Using a while loop:
i = 0
while i < len(list1):
  print(list1[i])
  i += 1
print('\n')

# LIST COMPREHENSIONS:
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# The Syntax:
# [expression for item in iterable if condition == True]

# Looping Using List Comprehension:
print('Looping Using List Comprehension:')
[print(i) for i in list1]

# Example: Based on a list of fruits, you want a new list, containing only the fruits with the letter 'e' in the name.
fruits = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
newFruits = []
for i in fruits:
  if 'e' in i:
    newFruits.append(i)
print(newFruits)

# With list comprehension you can do all that in one line:
print('\nList comprehension:')
newFruits = [i for i in fruits if 'e' in i]
print(newFruits)

# The condition is optional and can be omitted:
print('\nCondition omitted:')
newFruits = [i for i in fruits]
print(newFruits)

# ITERABLE

# Can use the range() function:
newList = [i for i in range(10)]
print(newList)

# Same example, but with a condition:
newList = [i for i in range(10) if i % 2 == 0]
print('Pair numbers:', newList)

# EXPRESSION
# Manipulate before it ends up in the list:
newList = [i.upper() for i in fruits]
print(newList)

# Set the outcome to whatever you like:
newList = [i.upper() if i.startswith('m') else i.lower() for i in fruits]
print(newList)

# SORT LIST - List Alphanumerically:

# Sort the list alphabetically:
newList = sorted(fruits) # sorted() function sorts the list in place.
print('Alphabetically:', newList)
# Sort descending:
newList = sorted(fruits, reverse=True)
print('Descending:', newList)

# Sort th list numerically:
numList = [100, 50, 65, 82, 23]
numList.sort() # sort() function sorts the list in place.
print('Numerically:', numList)
# Sort descending:
numList.sort(reverse=True)
print('Descending:', numList)

# SORT LIST - Customize Sort Function:
# Using the keyword argument "key = function":
def myFunc(n):
  return abs(n - 50) # Return the absolute value of the difference between the number and 50.
numList.sort(key=myFunc)
print('Customized:', numList)

# SORT LIST - Case Insensitive Sort:
# Perform case-insensitive sort of the list:
fruits1 = ['banana', 'Orange', 'KIWI', 'apple', 'Mango']
print(fruits1)
newList = sorted(fruits1, key = str.lower)
print('Case-insensitive:', newList)

# SORT LIST - Reverse Order:
# The reverse() method reverses the current sorting order of the list.
fruits1.reverse()
print('Reverse Order:', fruits1)

# COPY A LIST
# The copy() method returns a shallow copy of the list:
newList = fruits.copy()
print('Shallow copy:', newList)

# The list() constructor returns a list from an iterable, a string:
newList = list(fruits)
print('List constructor:', newList)

# JOIN LIST

# Using the "+" operator:
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list3 = list1 + list2
print('Using the "+" operator:', list3)

# Using "append()" method:
for i in list2:
  list1.append(i)
print('Using "append()" method:', list1)

# Using "extend()" method:
listA = ['x', 'y', 'z']
listB = [4, 5, 6]
listA.extend(listB)
print('Using "extend()" method:', listA)