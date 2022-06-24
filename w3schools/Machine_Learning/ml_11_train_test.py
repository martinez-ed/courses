## Train/Test - Is a method to measure if the model is good enough to predict the data. A training set 80%, and a testing set 20%.

# Start with a data set.
#e.g. Data set of 100 customers in a shop, and their shopping habits:
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2) #set the seed

#number of minutes before making a purchase
x = np.random.normal(3, 1, 100)
#amount of money spent on the purchase
y = np.random.normal(150, 40, 100) / x 

plt.scatter(x, y) #plot the data
plt.show() #show the plot


## Split into Train/Test
# The training set should be a random selection of 80% of the original data. The testing set should be the remaining 20%:
train_x = x[:80] #first 80%
train_y = y[:80] #first 80%

test_x = x[80:] #the rest of the data
test_y = y[80:] #the rest of the data

plt.scatter(train_x, train_y, color='green') #plot the training data
plt.scatter(test_x, test_y, color='red') #plot the testing data
plt.show() #show the plot


## Fit the Data Set
#e.g. Draw a polynomial regression line through the data points:
myModel = np.poly1d(np.polyfit(train_x, train_y, 4)) #fit the data
myLine = np.linspace(0, 6, 100) #create a line

plt.scatter(train_x, train_y, color='green') #plot the training data
plt.scatter(test_x, test_y, color='red') #plot the testing data
plt.plot(myLine, myModel(myLine), color='blue') #plot the line
plt.show() #show the plot

# R-squared score (R2)
# The "sklearn" module has a "r2_score()" method that returns the R-squared score of the model.
from sklearn.metrics import r2_score

# Trainings data
r2 = r2_score(train_y, myModel(train_x)) #calculate the R-squared score
print(r2) #result: 0.799 shows that there is a OK relationship

# Testing data
r2 = r2_score(test_y, myModel(test_x)) #calculate the R-squared score
print(r2) 
#result: 0.809 shows that the model fits the testing set as well, and we are confident that we can use the model to predict the future data.


## Predict the future data
#e.g. How much money will a buying customer spend, if he stays in the shop for 5 minutes?:
predict = myModel(5) #predict the amount of money spent on the purchase
print(predict) 
#result: customer will spent $22.88 on the purchase
