import matplotlib.pyplot as plt
import numpy as np

## The "plot()" function is used to draw points(markers) in a diagram.
# Plotting x and y points
x = np.array([1, 8])
y = np.array([3, 9])
plt.plot(x, y)
plt.show()


## Plotting without line
# Use the shortcut string notation parameter "o", which means rings.
plt.plot(x, y, 'o')
plt.show()


## Multiple points
# E.g. Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10):
x = np.array([1, 2, 6, 8])
y = np.array([3, 8, 1, 10])
plt.plot(x, y)
plt.show()


## default x-points
#  If don't specify the x-axis points, they will get the default values 0, 1, 2, 3, etc, depending on the length of the y-axis points.
y = np.array([3, 8, 1, 10, 5, 7])
plt.plot(y)
plt.show()
