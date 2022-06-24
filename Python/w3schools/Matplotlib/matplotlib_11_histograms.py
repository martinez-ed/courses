import matplotlib.pyplot as plt
import numpy as np

## A histogram is a graphical representation of the distribution of a dataset.
# Use the "hist()" function to draw histograms.

# Syntax: plt.hist(x, bins=10, range=None, normed=False, weights=None, color=None, label=None, stacked=False)

#e.g. Say you ask for the height of 250 people; a normal Data Distribution by NumPy:
x = np.random.normal(170, 10, 250) # Create 250 random numbers with a mean of 170 and a standard deviation of 10

plt.hist(x, bins=10) # Draw a histogram
plt.show()
