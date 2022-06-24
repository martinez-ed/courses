import matplotlib.pyplot as plt
import numpy as np

y = np.array([3, 8, 1, 10, 5, 7])

## Markers
#  The "marker" parameter is used to emphasize each point with a specified marker. The default marker is a dot.
#  "." - point
#  "," - pixel
#  "o" - circle
#  "v" - triangle down
#  "^" - triangle up
#  "<" - triangle left
#  ">" - triangle right
#  "1" - tri down + left
#  "2" - tri down + right
#  "3" - tri up + left
#  "4" - tri up + right
#  "8" - octagon
#  "s" - square
#  "p" - pentagon
#  "*" - star
#  "h" - hexagon1
#  "H" - hexagon2
#  "+" - plus
#  "x" - x
#  "D" - diamond
#  "d" - thin_diamond
#  "|" - vline
#  "_" - hline
#  "P" - pixel

# E.g. Mark each point with a "square" marker:
plt.plot(y, marker = 's')
plt.show()


## Format String "fmt"
# The "fmt" parameter is used to specify the format of the data in the diagram.
# Syntax: marker|line|color

# Line Reference:
#  "-" - solid line
#  "--" - dashed line
#  "-." - dash-dot line
#  ":" - dotted line

# Color Reference:
#  "b" - blue
#  "g" - green
#  "r" - red
#  "c" - cyan
#  "m" - magenta
#  "y" - yellow
#  "k" - black
#  "w" - white

plt.plot(y, 'P:r') # marker = 'P', line = ':', color = 'r'
plt.show()


## Marker Size
# The "markersize" parameter is used to specify the size of the marker. Shorter version "ms".
# The default size is 6.
plt.plot(y, '*-.y', ms = 15) # marker = star, line = dash-dot, color = yellow
plt.show()


## Marker color
# The "markeredgecolor" parameter is used to specify the color of the marker edge. Shorter version "mec".
plt.plot(y, 'P--g', ms = 10, mec = 'r') # marker = pixel, line = dashed, color = green, marker edge color = red
plt.show()

# The "marketfacecolor" parameter is used to specify the color inside of the markers. Shorter version "mfc".
plt.plot(y, 's:b', ms = 13, mfc = 'y', mec = 'r') # marker = square, line = dotted, color = blue, marker face color = yellow, marker edge color = red
plt.show()

# Use hexadecimal color code
plt.plot(y, 's:k', ms =10, mec = '#000000', mfc = '#EDFF00') # marker = square, line = dotted, color = black, marker face color = yellow, marker edge color = black
plt.show()

# E.g. Mark each point with the color named "hotpink":
plt.plot(y, 'o--r', ms = 10, mec = 'r', mfc = 'hotpink') # marker = circle, line = dash-dot, color = red, marker edge color = red, marker face color = hotpink
plt.show()
