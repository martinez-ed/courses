import matplotlib.pyplot as plt
import numpy as np


## Scatter Plot
# Is a diagram where each value in the data set is represented by a dot.

# The "matplotlib.pyplot" module is used to create a scatter plot. It needs two arrays of the same length, one for the x-axis and one for the y-axis.

#e.g. Use the "scatter()" method to draw a scatter diagram:
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
plt.scatter(x, y)
plt.show()


## Random Data Distribution
#e.g. Create 2 arrays that are both filled with 1000 random numbers from a normal data distribution:
# - The first array will have the mean set to 5.0 and the standard deviation set to 1.0.
# - The second array will have the mean set to 10.0 and the standard deviation set to 2.0.
x = np.random.normal(5, 1, 1000)
y = np.random.normal(10, 2, 1000)
plt.scatter(x, y) # Draw a scatter diagram
plt.show()
