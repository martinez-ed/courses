import matplotlib.pyplot as plt
import numpy as np

y = np.array([3, 8, 2, 9, 5])

## Use "linestyle", or shorter "ls", to change the style of the plotted line.
plt.plot(y, linestyle = 'dotted')
plt.show()

# E.g. Use "dashed" to draw a line with a dash-dot pattern.
plt.plot(y, ls = 'dashed')
plt.show()


## Shorter Syntax
# "linestyle" - "ls"
# "solid" - "-"
# "dotted" - ":"
# "dashed" - "--"
# "dashdot" - "-."

plt.plot(y, ls = '-.') 
plt.show()


## Line Color
# "color" - "c"
# "red" - "r"
# "green" - "g"
# "blue" - "b"
# "cyan" - "c"
# "magenta" - "m"
# "yellow" - "y"
# "black" - "k"
# "white" - "w"

plt.plot(y, c = 'r')
plt.show()

#E.g. Use hexadecimal color code to specify the color of the line.
plt.plot(y, c = '#EDFF00')
plt.show()

#e.g. Plot with the color named "hotpink".
plt.plot(y, c = 'hotpink')
plt.show()


## Line Width
# "linewidth" - "lw"
plt.plot(y, lw = 20.5)
plt.show()


## Multiple Lines
#e.g. Draw two lines by specifying a "plt.plot()" function for each line, only specifying the points on the y-axis:
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)
plt.show()
