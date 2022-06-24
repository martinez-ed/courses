# An Iterator is an object that contains a countable number of values.

# Technically, an iterator is an object which implements the iterator protocol, which consist of the methods "__iter__()" and "__next__()".


## Iterator vs Iterable
# Use "iter()" to convert an iterable object into an iterator object.
myTuple = ('apple', 'banana', 'cherry')
myIter = iter(myTuple) # Create an iterator object

print(next(myIter)) # apple
print(next(myIter)) # banana
print(next(myIter)) # cherry

# Even strings are iterable objects, and can return an iterator:
myStr = 'banana'
myIter = iter(myStr) # Create an iterator from a string

print('\nString Iterator:')
print(next(myIter)) # b
print(next(myIter)) # a
print(next(myIter)) # n
print(next(myIter)) # a
print(next(myIter)) # n
print(next(myIter)) # a


## Loping Through an Iterator
# The "for" loop actually creates an iterator object and executes the "next()" method for each loop.


## Create an iterator object:
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

nums = MyNumbers() # Create an instance of the iterator
myIter = iter(nums) # Create an iterator object

print('\nIterator Object:')
for x in myIter: # Loop through the nums
  print(x, end=' ') # Print the nums
  if x > 5: # Stop the loop
    break # when x > 5


## StopIteration
# In the "__next__()" method, we can add a terminating condition to the loop.
print('\nStopIteration:')
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20: # Stop after 20
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration # StopIteration is a built-in exception

nums = MyNumbers() # Create an instance of the iterator
myIter = iter(nums) # Create an iterator object

for x in myIter: # Loop until StopIteration is raised
  print(x, end=' ') # Print the values 1 to 20