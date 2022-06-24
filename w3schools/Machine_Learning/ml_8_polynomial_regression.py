import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score


## Polynomial Regression
# Uses the relationship between the variables x and y to find the best way to draw a line through the data points.

#e.g. The arrays in the z axis represents the hours of the day and the y-axis represents the speed:

#create the arrays
hours = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
speed = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

#NumPy has a method that lets us make a polynomial model
myModel = np.poly1d(np.polyfit(hours, speed, 3)) #syntax: np.polyfit(x, y, degree)

#Specify how the line will display, start at 1 and end at 22
myLine = np.linspace(1, 22, 100) #syntax: np.linspace(start, end, number of points)

plt.scatter(hours, speed)
plt.plot(myLine, myModel(myLine))
plt.show()


## R-Squared
# The R-squared is a measure of how close the model is to the data.
# It is a value between 0 and 1.
# The closer the value is to 1, the better the model fits the data.

# Use "Sklearn" module to compute the R-squared:
# from sklearn.metrics import r2_score
print(r2_score(speed, myModel(hours))) #0.94 very good relationship


## Predict Future Values
#e.g. Predict the speed of a car that passed the tollbooth at around 17:00 P.M.:
myModel = np.poly1d(np.polyfit(hours, speed, 3))
newSpeed = myModel(17)
print(newSpeed) #88.87


## Bad Fit for Polynomial Regression
x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

myModel = np.poly1d(np.polyfit(x, y, 3))
myLine = np.linspace(2, 95, 100) #syntax: np.linspace(start, end, number of points)

plt.scatter(x, y)
plt.plot(myLine, myModel(myLine))
plt.show()

#Very low r-squared value.
print(r2_score(y, myModel(x))) #0.00995
