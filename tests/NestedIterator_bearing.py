# Implemented an iterator to flatten it:
#
# NestedIterator(List) Initializes the iterator.
# int next() Returns the next integer in the nested list.
# boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.

# Implemented an iterator to flatten it:
class NestedIterator(object):
  def __init__(self, nestedList): # Initialize your data structure here.
    self.stack = [] # Stack to store the nestedList.
    self.pushAll(nestedList) # Push all the integers of the nestedList into the stack.
    self.stack.reverse() # Reverse the stack to make it LIFO.

  # Check if the current element is a list.
  def isList(self, nestedList):
    return isinstance(nestedList, list)

  # Check if the current element is an integer.
  def isInteger(self, nestedList):
    return isinstance(nestedList, int)

  # Get the integer of the current element.
  def getInteger(self, nestedList):
    return nestedList if self.isInteger(nestedList) else None

  def next(self):
    # Return the next element in the iteration
    return self.stack.pop()

  def hasNext(self):
    # Return true if there is a next element or false if there is not.
    return len(self.stack) > 0 # Check if the stack is empty.

  def pushAll(self, nestedList):
    # Push all the integers of the nestedList into the stack.
    for i in range(len(nestedList)): # Loop through the nestedList.
      if self.isList(nestedList[i]): # Check if the current element is a list.
        self.pushAll(nestedList[i]) # Push all the integers of the nestedList into the stack.
      else:
        self.stack.append(self.getInteger(nestedList[i])) # Push the integer of the current element into the stack.
      
# Your NestedIterator object will be instantiated and called as such:
nestedList = [1, [2, [3, 4, 23], [4, [5, 7, 8]]]]
i, v = NestedIterator(nestedList), []
while i.hasNext(): v.append(i.next())
print(v)
