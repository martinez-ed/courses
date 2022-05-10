import numpy as np

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

## Percentiles
# Use in statistics to give you a number that describes the value that a given percent of the values are lower than.

#e.g. Use the NumPy "percentile()" method to find the 25th and 75th percentiles of the data:
# x = np.percentile(ages, [25,75])
x = np.percentile(ages, 75)
print(x) # x = 43.0

#e.g. What is the age that 90% of the people are younger than?:
x = np.percentile(ages, 90)
print(x) # x = 61.0
