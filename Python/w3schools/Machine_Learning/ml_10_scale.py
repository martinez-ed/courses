import pandas as pd
# Sklearn module has a "StandardScaler()" method that return a Scaler object with methods for transforming data sets.
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler


## Scale
# When your data has different values, and even different measurement units, it can be dificult to compare them. We can scale data into new values that are easier to compare.

## Standardization
# formula: z = (x - mean) / standard deviation


#e.g. Scale the values in the Weight and Volume (values in liters instead of cm3) columns:
scale = StandardScaler() #create a scaler object

df = pd.read_csv('cars2.csv') #read the data
X = df[['Weight', 'Volume']] #independent values
y = df['CO2'] #dependent values

scaledX = scale.fit_transform(X) #fit the scaler object to the data and transform it
print(scaledX)


#e.g. Predict the CO2 emission from a 1.3 liter car that weighs 2300kg:
regr = linear_model.LinearRegression() #regression object
regr.fit(scaledX, y) #fit the model

scaled = scale.transform([[2300, 1.3]]) #transform the data

predictC02 = regr.predict([scaled[0]]) #predict the CO2 emission
print(predictC02) #value: [107.2087328]
