import numpy as np

## Machine Learning, analysis of data, and prediction of future outcomes.

## Data Types

# 1. Numerical - data are numbers.
#     e.g. 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#   Discrete data:
#     - numbers that are limited to integers. 
#       e.g. The of cars passing by.
#   Continuous data:
#     - numbers that are of inifinite value.
#       e.g. The price of an item, or the size of an item. 

# 2. Categorical - data are values that cannot be measured up against each other.
#     e.g. A color value, or any yes/no values.

# 3. Ordinal - data are like categorical data, but can be measured up against each other.
#     e.g. School grades where A is better than B, and so on.


## Mean, Median and Mode
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# 1. Mean - the average of all the values in a set.
# To calculate the mean, find the sum of all values, and divide the sum by the number of values. e.g. (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10) / 10 = 5.5
# Use the NumPy "mean()" method to find the average speed.
x = np.mean(speed)
print(x) # x = 89.76923076923077

# 2. Median - the middle value in a set, after it has been sorted.
# If there are 2 numbers in the middle, divide the sum of those numbers by 2.
# Use the NumPy "median()" method to find the middle value:
x = np.median(speed)
print(x) # x = 87.0

# 3. Mode - the most common value in a set.
# Use the SciPy "mode()" method to find the number that appears the most.
from scipy import stats as st

# The "mode()" method returns a ModeResult object tha contain the mode number, and the count of how many times it appears.
x = st.mode(speed)
print(x) #ModeResult(mode=array([86]), count=array([3]))
