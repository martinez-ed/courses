# Built-in package called "json", which can be used to work with JSON data.

## Import the "json" module:
import json


## Parse JSON - convert from JSON to Python:
# The "json.loads()" function converts a JSON string to a Python object:

# some JSON:
x = '{"name": "John", "age": 30, "city": "New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y['city']) # New York


## Convert Python objects to JSON:
# The "json.dumps()" function converts a Python object to a JSON string:

# a Python object (dict):
x = {
  'name': 'John',
  'age': 30,
  'city': 'Bogota'
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y) # {"name": "John", "age": 30, "city": "Bogota"}


## Convert Python objects into JSON strings:
print(json.dumps({"name": "John", "age": 30})) #dict
print(json.dumps(["apple", "bananas"])) #list
print(json.dumps(("apple", "bananas"))) #tuple
print(json.dumps("hello")) #string
print(json.dumps(42)) #int
print(json.dumps(31.76)) #float
print(json.dumps(True)) #boolean
print(json.dumps(False)) #boolean
print(json.dumps(None)) #null


## Convert a Python object containing all the legal data types:
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))


## Format the Result:
# Use the "indent" parameter to format the result:
ft = json.dumps(x, indent = 2)
print('\nFormat the Result:\n', ft)

# Use the "separators" parameter to change the default separators:
ft = json.dumps(x, indent = 2, separators = (" ", " => "))
print('\nChange separators:\n', ft)

# Use the "sort_keys" parameter to specify if the result should be sorted or not:
ft = json.dumps(x, indent = 2, sort_keys = True)
print('\nSort the Result:\n', ft)