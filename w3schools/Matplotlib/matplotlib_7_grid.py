import matplotlib.pyplot as plt
import numpy as np

x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([40, 80, 34, 93, 14, 55, 67, 90, 45, 67])


## Use the "grid()" function to add grid lines to the plot.

# plt.plot(x, y, 's') # Plot the data as a scatter plot.
plt.plot(x, y) # Plot the data as a line plot.
plt.grid(True) # Add grid lines to the plot.
plt.show() # Display the plot.


## Specify which grid lines to display.
plt.plot(x, y, 's') # Plot the data as a scatter plot.
plt.grid(axis='y') # Grid lines for the y-axis.
plt.show()


## Set line properties for the grid.
# Properties: color as "c" (default is black), linewidth as "lw" (default is 1.0), linestyle as "ls" (default is solid).
plt.plot(x, y)
plt.grid(c='r', ls='--', lw=2) # Set the grid line properties.
plt.show()
