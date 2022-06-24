# string format()
# Syntax:
#   string.format(value, value, ...)


# The "format()" method is used to format a string.
price = 49
txt = 'The price is {} dollars'
print(txt.format(price))

# E.g. Format the price to be displayed as a number with two decimals:
txt = 'The price is {:.2f} dollars'
print(txt.format(price)) # 49.00


## Multiple values
itemno = 567
price = 49000
qty = 3
myorder = 'I want {} pieces of item number {} for {:.2f} dollars.'
print(myorder.format(qty, itemno, price)) # I want 3 pieces of item number 567 for 49000.00


## Index Numbers
myorder = 'I want to pay ${1:,.2f} dollars for {2} pieces of item {0}.'
print(myorder.format(itemno, price, qty)) # I want to pay $49,000.00 dollars for 3 pieces of item 567.


## Named Indexes
txt = 'I have a {carname}, it is a {model}.'
print(txt.format(carname='Ford', model='Mustang')) # I have a Ford, it is a Mustang.
