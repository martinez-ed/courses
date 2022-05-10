# Getting the data type:
x = 5
print(type(x)) # <class 'int'>

x = ['apple', 'banana', 'cherry']
print(type(x)) # <class 'list'>

x = ('apple', 'banana', 'cherry')
print(type(x)) # <class 'tuple'>

x = {'name': 'John', 'age': 36}
print(type(x)) # <class 'dict'>

x = {'apple', 'banana', 'cherry'}
print(type(x)) # <class 'set'>

x = range(6)
print(type(x)) # <class 'range'>

x = True
print(type(x)) # <class 'bool'>

# Setting the data type:
x = str('Hello World') 
print(x) # Hello World

x = list(('apple', 'banana', 'cherry'))
print(x) # ['apple', 'banana', 'cherry']

x = dict(name='John', age=36)
print(x) # {'name': 'John', 'age': 36}

x = bytes(5)
print(x) # b'\x00\x00\x00\x00\x00'

x = bytearray(5)
print(x) # bytearray(b'\x00\x00\x00\x00\x00')

x = memoryview(bytes(5))
print(x) # <memory at 0x7f8b8b8b8b90>