## Regression
# Is used when you yty yo find the relationship between variables.

## Linear Regression
# Uses the relationship between the data-points to draw a straight line through all them.

#e.g. We have registered the age and speed of 13 cars as they were passing a tollbooth. The x-axis is the age and the y-axis is the speed. Use linear regression to collect the data:

import matplotlib.pyplot as plt
from scipy import stats #draw the line of Linear Regression

x = [5,7,8,7,2,17,2,9,4,11,12,9,6] #age
y = [99,86,87,88,111,86,103,87,94,78,77,85,86] #speed

# Execute a method that returns some important key values of Linear Regression:
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

# Use the "slope" and "intercept" values to return a new value that represents where on the y-axis the corresponding x value will be placed:
def myfunc(x):
  return slope * x + intercept

# Run each value of the x array through the function. This will result in a new array with new values for the y-axis:
mymodel = list(map(myfunc, x))

# Draw the original scatter plot:
plt.scatter(x, y)
# Draw the line of Linear Regression:
plt.plot(x, mymodel)
# Display the diagram:
plt.show()


## R for Relationship
# Is used to determine the relationship between two variables.
print(r_value)


## Predict Future Values
#e.g. Predict the speed of a 10 years old car:
speed = myfunc(10)
print(speed) # 85.59308314937454


## Bad Fit
#e.g. The data is not well-suited for the model.
x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunct(x):
  return slope * x + intercept

mymodel = list(map(myfunct, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

print(r) #bad fit 0.01331814154297491
