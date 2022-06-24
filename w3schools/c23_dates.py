# Import a module named "datetime" to work with dates as dates objects.
import datetime

x = datetime.datetime.now()  # Get the current date and time.
print(x)

# E.g. return the year and name of weekday:
print('Year:', x.year)
print('Weekday:', x.strftime('%A'))


## Creating Date Object.
# Use the "datetime()" class constructor of the "datetime" module.

# import datetime

x = datetime.datetime(2020, 5, 17)
print('Date Object:', x)


## The "strftime()" method.
# import datetime

x = datetime.datetime(2020, 5, 17)
print('\n"strftime()" method:', x.strftime('%A, %B %d, %Y'))