import numpy as np

speed = [86,87,88,86,87,85,86]

## Standard Deviation
# Describes how spread out the values are.

# Low standard deviation means that most of the numbers are close to the mean (average) value.
# High standard deviation means that the values are spread out over a wider range.

#e.g. Use the NumPy "std()" method to find the standard deviation:
x = np.std(speed)
print(x) # x = 0.9035079029052513

#e.g. Standar deviation of a numbers with a wider range:
speed = [32,111,138,28,59,77,97]

x = np.std(speed)
print(x) # x = 37.84501153334721


## Variance
# Describes how spread out the values are.
# Use the NumPy "var()" method to find the variance:
x = np.var(speed)
print(x) # x = 1432.2448979591834
