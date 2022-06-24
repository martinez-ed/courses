# Dictionaries are used to store data values in "key: value" pairs.

# Create and print a dictionary:
myDict = {
  'name': 'John', 
  'age': 23,
  'is_student': True
}
print(myDict)

# Print the "age" value of the dictionary:
print('Value of \"age\":', myDict['age'])

# Dictionary length:
print('Length of dictionary:', len(myDict))

# Data types:
myDict = {
  'name': 'John',
  'age': 23,
  'is_student': True,
  'courses': ['Math', 'Physics', 'CompSci']
}
print(myDict)
print('Data type of \"name\":', type(myDict['name']))


## ACCESSING DATA:
# Get the value of the "model" key:
x = myDict['courses']
print('Value of \"courses\":', x)

# Use "get()" method to give the same result:
x = myDict.get('age')
print('Value of \"age\":', x)

# Get Keys:
print('Keys:', myDict.keys())

# E.g. Add a new item to the dictionary and see the keys update:
myDict['last_name'] = 'Smith'
print('After:', myDict.keys())

# Get Values:
print('Values:', myDict.values())

# E.g. Make change in the dictionary and see the values update:
myDict['age'] = 40  # Change the value of the "age" key
print('After:', myDict.values())

# Use "items()" method to get the key-value pairs, as tuple in a list:
print('\nKey-value pairs:', myDict.items())

# E.g. Make a change in the original dictionary and see the key-value pairs update:
x = myDict.items()
print('\nBefore:', x) # Before the change
myDict['last_name'] = 'Martínez'  # Change the value of the "age" key
print('\nAfter:', x)  # After the change

# Check if a key exists:
print('\nDoes \"age\" key exist?\n', 'age' in myDict)


## CHANGING DATA:
# You can change the value of a specific item by referring to its key name:
myDict['age'] = 31
print('\nChange value:\n', myDict)

# Update the dictionary:
myDict.update({'age': 32, 'last_name': 'García'})
print('\nUpdate:\n', myDict)


## ADDING DATA:
# Use a new index key and assign a value to it:
myDict['phone'] = '555-1234'
print('\nAdd new key-value pair:\n', myDict)

# Use "update()" method to add new key-value pairs:
myDict.update({'phone': '555-4321', 'last_name': 'Roncancio'})
print('\nUpdate:\n', myDict)


## REMOVING DATA:
# Use "pop()" method to remove a key-value pair:
myDict.pop('phone')
print('\nRemove key-value pair:\n', myDict)

# Use "popitem()" method to remove the last key-value pair:
myDict.popitem()
print('\nRemove last key-value pair:\n', myDict)

# Use "del" to remove the item with the specified key name:
del myDict['age']
print('\nRemove item with key name:\n', myDict)

# The "del" keyword can also be used to delete the dictionary completely:
# del myDict
# print('\nRemove dictionary:\n', myDict)  # Error: NameError: name 'myDict' is not defined

# Use "clear()" method to empty the dictionary:
myDict.clear()
print('\nClear dictionary:\n', myDict)


## LOOPING OVER DICTIONARIES:
print('\nLOOPING OVER DICTIONARIES')

myDict = {
  'name': 'John',
  'age': 23,
  'is_student': True,
  'courses': ['Math', 'Physics', 'CompSci']
}

# Usign "for" loop:
print('\nUsing \"for\" loop:')
for key in myDict:
  print(key, ':', myDict[key]) # Prints the key and the value

# Using "values()" method:
print('\nUsing \"values()\" method:')
for value in myDict.values():
  print(value)

# Using "keys()" method:
print('\nUsing \"keys()\" method:')
for key in myDict.keys():
  print(key)

# Using "items()" method:
print('\nUsing \"items()\" method:')
for key, value in myDict.items():
  print(key, ':', value)


## COPYING DICTIONARIES:
print('\nCOPYING DICTIONARIES')

# Use "copy()" method to create a copy of the dictionary:
myDict2 = myDict.copy()
print('\nCopy with copy method:\n', myDict2)

# Use "dict()" method to create a copy of the dictionary:
myDict3 = dict(myDict)
print('\nCopy with dict method:\n', myDict3)


## NESTED DICTIONARIES:
# Create a dictionary that contain three dictionaries:
myFamily = {
  'child1': {
    'name': 'Emma',
    'last_name': 'Martinez',
    'age': 7
  },
  'child2': {
    'name': 'Olivia',
    'last_name': 'Roncancio',
    'age': 34
  },
  'child3': {
    'name': 'Sophia',
    'last_name': 'García',
    'age': 39
  }
}
print('\nNested dictionary:\n', myFamily)

# Add three dictionaries into a new dictionary:
myCompany = {
  'name': 'Google',
  'address': '1600 Amphitheatre Parkway',
  'employees': myFamily
}
myTools = {
  'name': 'Python',
  'version': '3.7.0',
  'company': myCompany
}

myLife = {
  'myfamyly' : myFamily,
  'mytools' : myTools,
  'mycompany' : myCompany
}
print('\nNested dictionary:\n', myLife)


## METHODS:
# Use "fromkeys()" method to create a dictionary with the specified keys and values:
print('\nUse \"fromkeys()\" method:')

names = ['John', 'Mary', 'Mark', 'Sarah', 'Sophia'] # Create a list of names
print(names)
status = 0
data = dict.fromkeys(names, status)
print(data)

# Use "get()" method to get the value of a specific key:
print('\nUse \"get()\" method:\n', data.get('Ed', 'nuevo'))
print(data)

# Use "setdefault()" method to set a default value for a specific key; if the key does not exist, it will be added:
print('\nUse \"setdefault()\" method:\n', data.setdefault('Ed', 'nuevo2'))
print(data)