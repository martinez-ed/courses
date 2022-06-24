from calendar import c
import matplotlib.pyplot as plt
import numpy as np

## Creating Bars
# Use the "bar()" function to draw bars graphs.

#e.g. Draw 4 bars:
x = np.array(['A', 'B', 'C', 'D'])
y = np.array([3, 8, 1, 10])

plt.bar(x, y) # Draw a bar graph
plt.show()


## Horizontal Bars
# Use the "barh()" function to draw horizontal bars graphs.
plt.barh(x, y) # Draw a horizontal bar graph
plt.show()


## Bar Color
# The "bar()" and "barh()" takes the keyword argument "color" to set the color of the bars.
plt.bar(x, y, color='r') # Set the color of the bars to red
plt.show()

#e.g. Draw 4 bars with different colors:
x = np.array(['A', 'B', 'C', 'D'])
y = np.array([3, 8, 1, 10])
plt.bar(x, y, color=['r', 'g', 'b', 'y']) # Set the color of the bars to red, green, blue and yellow
plt.show()

#e.g. Use hexadecimal color value:
plt.bar(x, y, color='#EDFF00') # Set the color of the bars to yellow
plt.show()


## Bar width
# The default width of the bars is 0.8.
# Use the argument "width" to set the width of the bars.
plt.bar(x, y, color='k', width=0.1) # Set the width of the bars to 0.5
plt.show()


## Bar Height
# The "barh()" takes the keyword argument "height" to set the height of the bars.
plt.barh(x, y, height=0.3) # Set the height of the bars to 0.3
plt.show()
