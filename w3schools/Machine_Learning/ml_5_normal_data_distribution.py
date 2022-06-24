import numpy as np
import matplotlib.pyplot as plt


## Normal Data Distribution
# Values are concentred around a given value.

# Use a numpy method "random.normal()" to create a typical data distribution:
x = np.random.normal(5.0, 1.0, 100000) #syntax: np.random.normal(loc, scale, size)

plt.hist(x, 100) # 100 bars
plt.show()
