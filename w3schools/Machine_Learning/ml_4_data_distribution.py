import numpy as np
import matplotlib.pyplot as plt

# How can we get Big Data Sets?
# To create a data sets for testing, we use the Python module "NumPy", which comes with a number of methods to create random data sets, of any size.

#e.g. Create an array containig 250 random floats between 0 and 5:
x = np.random.uniform(0.0, 5.0, 250) #syntax: np.random.uniform(low, high, size)
print(x)


## Histogram
# Use the matplotlib module "pyplot" to create a histogram of the data with the "hist()" method:
plt.hist(x, 5)
plt.show()


## Big Data Distributions
#e.g. Create an array with 100000 random numbers, and display them using a histogram with 100 bars:
x = np.random.uniform(0.0, 5.0, 100000)
plt.hist(x, 100)
plt.show()
