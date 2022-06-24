import matplotlib.pyplot as plt
import numpy as np

## Display multiple plots.
# With the "subplot()" function, you can display multiple plots on the same figure.

# Syntax: plt.subplot(nrows, ncols, plot_number)

#plot 1:
x = np.array([0, 1, 4, 9, 16])
y = np.array([3, 8, 1, 10, 2])
plt.subplot(1, 2, 1) # Create a subplot with 1 row and 2 columns, and the first plot.
plt.plot(x, y)

#plot 2:
x = np.array([0, 1, 4, 9, 16])
y = np.array([10, 20, 30, 40, 50])
plt.subplot(1, 2, 2) # Create a subplot with 1 row and 2 columns, and the second plot.
plt.plot(x, y)

plt.show()

#e.g. Draw 2 plots "on top" of each other.

#plot 1:
plt.subplot(2, 1, 1) # Create a subplot with 2 rows and 1 column, and the first plot.
plt.plot(x, y)

#plot 2:
plt.subplot(2, 1, 2) # Create a subplot with 2 rows and 1 column, and the second plot.
plt.plot(x, y)

plt.show()


## Title.
# The "title()" function sets the title of the figure.
# The "xlabel()" and "ylabel()" functions set the x- and y-axis labels.
# The "legend()" function adds a legend to the figure.

#plot 1:
plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title('SALES')
#plot 2:
plt.subplot(1, 2, 2)
plt.plot(x, y, 'r', '--')
plt.title('INCOME')

plt.show()


## Super Title.
# The "suptitle()" function sets the super title of the figure.

#plot 1:
plt.subplot(2, 1, 1)
plt.plot(x, y, c='r', ls='--', marker='s', ms=10, mew=2, lw=2)
plt.title('SALES')
#plot 2:
plt.subplot(2, 1, 2)
plt.plot(x, y, c='k', ls='-.')
plt.title('INCOME', c='r', fontsize=10, loc='left')

plt.suptitle('My Shopping Cart')
plt.show()
