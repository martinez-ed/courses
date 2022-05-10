# Python does not have built-in support for arrays, but "List" can be used instead.

# Arrays are used to store multiple values in one single variable:
cars = ['bmw', 'audi', 'toyota', 'subaru']

# Get the value of the first array element:
print(cars[0])

# Modify the value of the first array element:
cars[0] = 'Mercedes'
print(cars)

# The length of the array:
print(len(cars))


# Looping array elements:
# Use the " for in" loop to loop through the array:
for car in cars:
  print(car, end=' | ')
print('\n')


# Adding array elements:
# Use the "append" method to add new elements to the array:
cars.append('Honda')
print(cars)


# Removing array elements:
# Use the "pop" method to remove the last element of the array:
cars.pop()
print(cars)
print(cars.pop(1)) # Remove the element at index 1
print(cars)

# Use the "remove()" method to remove an element from the array:
cars.remove('toyota')
print(cars)