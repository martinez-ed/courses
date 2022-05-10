import matplotlib.pyplot as plt
import numpy as np

#data. Result of 13 cars passing by.
# X-axis - Age of the car
# Y-axis - Speed of the car
#day one, the age and the speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])


## Creating scatter plot
# The "scatter()" function plots one dot for each observation. It needs 2 arrays of the same length.
plt.scatter(x,y)
plt.show()

#data. Are there any realitionship between the observation?
#--> It seems that the newer car, the fast it drives.


## Compare Plots
#e.g. Draw 2 plots on the same figure:

#day one, the age and the speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)

#day two, the age and the speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, c='#EDFF00')

plt.show()
#--> Conclusion: After comparing the two plots, we can see that the older cars are slower.


## Color each dot
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

#e.g. Using an array of color as value for the "c" argument:
colors = np.array(['red', 'green', 'blue', 'yellow', 'black', 'orange', 'purple', 'brown', 'pink', 'grey', 'cyan', 'magenta', 'lime'])
plt.scatter(x, y, c=colors)
plt.show()


## ColorMap
# Using a colormap as value for the "cmap" argument:
# Built-in colormaps e.g.:
# "Accent", "viridis", "plasma", "inferno", "magma", "cividis"
# "Blues", "BuGn", "BuPu", "GnBu", "Greens", "Greys", "Oranges", "OrRd", "PuBu", "PuBuGn", "PuRd", "Purples", "RdPu", "Reds", "YlGn", "YlGnBu", "YlOrBr", "YlOrRd", "autumn", "bone", "cool", "copper", "gist_earth", "gist_gray", "gist_heat", "gist_ncar", "gist_rainbow", "gist_stern", "gray", "hot", "hsv", "jet", "pink", "spring", "summer", "winter", "BrBG", "bwr", "coolwarm", "PiYG", "PRGn", "PuOr", "RdBu", "RdGy", "RdYlBu", "RdYlGn", "Spectral", "seismic", "Accent", "Dark2", "Paired", "Pastel1", "Pastel2", "Set1", "Set2", "Set3", "gist_yarg", "gist_gray", "terrain", "ocean", "gist_ncar", "gist_rainbow", "gist_stern", "brg", "CMRmap", "cubehelix", "gnuplot", "gnuplot2", "gist_earth", "gist_gray", "terrain", "ocean", "gist_ncar", "gist_rainbow", "gist_stern", "brg", "CMRmap", "cubehelix", "gnuplot", "gnuplot2", "gist_earth", "gist_gray", "terrain", "ocean", "gist_ncar", "gist_rainbow", "gist_stern", "brg", "CMRmap", "cubehelix", "gnuplot", "gnuplot2", "gist_earth", "gist_gray", "terrain", "ocean", "gist_ncar", "gist_rainbow", "gist_stern", "brg", "CMRmap", "cubehelix", "gnuplot", "gnuplot2", "gist_earth", "gist_gray", "terrain", "ocean", "gist_ncar", "gist_rainbow", "gist_stern", "brg", "CMRmap", "cubehelix", "gnuplot", "gnuplot2", "gist_earth", "gist_gray", "terrain", "ocean", "gist_ncar", "gist_rainbow", "gist_stern", "brg", "CMRmap", "cubehelix", "gnuplot", "gnuplot2", "gist_earth", "gist_gray", "terrain", "ocean.

#e.g. Create a color array, and specify a colormap "viridis" in the scatter plot:
color = np.array([0,10,20,30,40,45,50,55,60,70,80,90,100])
plt.scatter(x, y, c=color, cmap='viridis')
plt.colorbar() # Add a colorbar to the scatter plot.
plt.show()

#e.g. use another colormap and "random values":
# Syntax "random.randint(low, high, size)"
x = np.random.randint(100, size=100)
y = np.random.randint(100, size=100)
color = np.random.randint(100, size=100)

plt.scatter(x, y, c=color, cmap='CMRmap')
plt.colorbar()
plt.show()


## Size of the dots
# Use the "s" argument to specify the size of the dots:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes) #set the size of the dots.
plt.grid(axis='y', c='black', ls='--', lw=0.5)
plt.show()


## Alpha (transparency)
# Use the "alpha" argument to specify the transparency of the dots:
plt.scatter(x, y, s=sizes, alpha=0.4)
plt.grid(c='g', ls='--', lw=0.5)
plt.show()


## Combine color, size and transparency
#e.g. Create random arrays with 100 values for x-points, y-points, color and size:
x = np.random.randint(100, size=100)
y = np.random.randint(100, size=100)
color = np.random.randint(100, size=100)
sizes = 10 * np.random.randint(100, size=100)

plt.scatter(x, y, s=sizes, c=color, alpha=0.4, cmap='nipy_spectral')
plt.grid(c='k', ls='--', lw=0.5)
plt.colorbar()
plt.show()
