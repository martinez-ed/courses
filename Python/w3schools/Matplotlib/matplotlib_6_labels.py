import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([3, 8, 2, 9, 5, 6, 7, 8, 9, 10])


## Create labels for a Plot
# Use the "xlabel()" and "ylabel()" functions to add labels to the x- and y-axes.
plt.plot(x, y)
plt.xlabel('Fundraising time')
plt.ylabel('Fundraising amount')
plt.show()


## Create a Title for a Plot
# Use the "title()" function to add a title to the plot.
plt.plot(x, y)
plt.title('Fundraising over time')
plt.xlabel('Timeline')
plt.ylabel('Amount raised')
plt.show()


## Set Font Properties for title and labels
font1 = {'family': 'serif', 'color': 'blue', 'weight': 'bold', 'size': '20'}
font2 = {'family': 'serif', 'color': 'darkred', 'weight': 'normal', 'size': '12'}

plt.title('Fundraising over time', font1)
plt.xlabel('Timeline', font2)
plt.ylabel('Amount raised', font2)
plt.plot(x, y)
plt.show()


## Position the title and labels
# Use the "loc" and "bbox" parameters to position the title and labels.
plt.title('Fundraising over time', font1, loc='left')
plt.xlabel('Timeline', font2, loc='right')
plt.ylabel('Amount raised', font2, loc='top')
plt.plot(x, y)
plt.show()