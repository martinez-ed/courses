# Pyplot submodule is a utility module that provides access to the matplotlib plotting library.

# Import "pyplot" usually imported under the "plt" alias:
import matplotlib.pyplot as plt

# "numpy" is a Python package for scientific computing.
import numpy as np

# E.g. Draw a line in a diagram form position (0,0) to position (6,250):
x = np.array([0, 6])
y = np.array([0, 250])
plt.plot(x, y)
plt.show()