import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

# Use the "pie()" function to draw pie charts.

# Syntax: plt.pie(x, explode=None, labels=None, colors=None, autopct=None, pctdistance=0.6, shadow=True, labeldistance=1.1, startangle=None, radius=None, counterclock=True, wedgeprops=None, textprops=None, center=(0, 0), frame=True, rotatelabels=False)

plt.pie(y)
plt.show()


## Labels
# Use the "label" parameter, must be an array with one label for each wedge.
mylabels = ['Apple', 'Banana', 'Cherry', 'Date']
plt.pie(y, labels=mylabels)
plt.show()


## Start Angle
# Use the "startangle" parameter to rotate the first slice of the pie chart.
plt.pie(y, labels=mylabels, startangle=90)
plt.show()


## Explode
# Use the "explode" parameter to make slices of the pie chart explode.
myexplode = [0.2, 0.1, 0, 0]
plt.pie(y, explode=myexplode, labels=mylabels, startangle=90)
plt.show()


## Shadow
# Use the "shadow" parameter to draw a shadow behind the pie chart.
plt.pie(y, explode=myexplode, labels=mylabels, shadow=True, startangle=90)
plt.show()


## Colors
# Use the "colors" parameter to specify the colors of the pie slices.
mycolors = ['black', 'hotpink', 'b', '#EDFF00']
plt.pie(y, explode=myexplode, labels=mylabels, colors=mycolors)
plt.show()


## Legend
# Use the "legend()" parameter to display a legend.
plt.pie(y, explode=myexplode, labels=mylabels, colors=mycolors)
plt.legend(mylabels, loc='upper left')
plt.show()

# Legend with header
# The "title" parameter can be used to add a header to the legend.
plt.pie(y, explode=myexplode, labels=mylabels, colors=mycolors)
plt.legend(mylabels, loc='upper left', title='Four Fruits:')
plt.show()
