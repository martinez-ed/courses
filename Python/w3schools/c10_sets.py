# A "SET" is a collection which is unordered, unchangeable and unindexed.
# In Python sets are written with curly brackets.

# Create a set:
mySet = {'apple', 'banana', 'cherry'}
print(mySet)

# Duplicates are not allowed:
mySet = {'apple', 'banana', 'cherry', 'apple'}
print(mySet) # {'apple', 'banana', 'cherry'}

# Get the length of a set:
print(len(mySet)) # 3

# A set can contain different data types:
set1 = {'abc', 34, 'xyz', 'pqr'}
print(set1)
print(type(set1)) # <class 'set'>

# The "set()" Constructor:
set2 = set(('abc', 34, 'xyz', 'pqr')) # note the double round-brackets
print(set2)


# ACCESS SET ELEMENTS:

# You cannot access set elements by referring to an index, since sets are unordered the elements has no index.
names = {'john', 'jack', 'jill', 'james'}

# Loop through the set items using "for":
for i in names:
  print(i + ', is a member of the set.')

# Check if an element is in a set:
if 'john' in names:
  print('john is a member of the set.')
else:
  print('john is not a member of the set.')

# Chage items in a set:
# You cannot change items in a set, but you can add new items.


# ADD ITEMS
print('\n', 'ADD ITEMS:', '\n', names)

# Use the "add()" method to add new items:
name = 'jane'
names.add(name)
print('Add the name', name, 'in the set:', names)

# Use the "update()" method to add multiple items:
numbers = {1, 2, 3}
names.update(numbers)
print('Add the numbers', numbers, 'in the set:\n', names)

# Add Any Iterable (List, Tuple, Dict, Set, etc) to a Set:
myList = ['kiwi', 'mango', 'orange']
names.update(myList)
print('Add the list', myList, 'in the set:\n', names)


# REMOVE ITEMS
fruitsSet = {'apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango'}
print('\n', fruitsSet)

# Use the "remove()" method:
# If the item to remove does not exist, remove() will raise an error.
fruitsSet.remove('banana')
print('Remove the item "banana" from the set:\n', fruitsSet)

# Use the "discard()" method:
# If the item to remove does not exist, discard() will NOT raise an error.
fruitsSet.discard('banana') # no error
print(fruitsSet)

# Use the "pop()" method:
# The pop() method removes the last item. Sets are unordered, so you will not know which item that was removed.
x = fruitsSet.pop()
print(x)
print(fruitsSet)

# Use the "clear()" method:
# The clear() method empties the set.
fruitsSet.clear()
print(fruitsSet)

# Use the "del" keyword:
# The del keyword will delete the set completely.
del fruitsSet
# print(fruitsSet) # error


# LOOP SETS:
# Loop through the set items using "for":
fruitsSet = {'apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango'}
print('\n')
for i in fruitsSet:
  print(i)


# JOIN SETS:
# Both union() and update() will exclude any duplicate items.

# Use the "union()" method to join two or more sets:
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# Use the intersection_update() method to find the common items between two sets:
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
x.intersection_update(y)
print(x)

# Use the intersection() method to find the common items between two sets:
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
z = x.intersection(y) # variable z is a set
print(z)

# Use the symetric_difference_update() method to keep all items from both sets, but remove any duplicates:
x.symmetric_difference_update(y)
print(x)

# Use the "symmetric_difference()" method will return a new set, that contains only the elements that are NOT present in both sets:
z = x.symmetric_difference(y)
print(z)