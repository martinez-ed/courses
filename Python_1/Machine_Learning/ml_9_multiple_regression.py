import pandas as pd
from sklearn import linear_model


## Multiple Regression
# Is like a linear regression, but with more than one independent value, try to predict a value based on two or more variables.

# Use "Pandas" module to import, analyze, cleaning, exploring and manipulating data.
df = pd.read_csv('cars.csv') #read the data
X = df[['Weight', 'Volume']] #independent values
y = df['CO2'] #dependent values

# Create a "regression object" that are ready to predict "CO2" values based on a car's weight and volume: 
regr = linear_model.LinearRegression() #regression object
regr.fit(X, y) #fit the model

# Predict the CO2 emissions of a car where the weight is 2300kg and the volume is 1300cm3:
predictCO2 = regr.predict([[2300, 1300]])
print(predictCO2) #value: [107.2087328]

# Result explained: The predicted CO2 emissions of a car with weight 2300kg and volume 1300cm3 is 107 grams of CO2 for each km it drives.


## Coefficient - Is a factor that describes the relationship with an unknown variables.
#e.g. Print the coeffiecient value of the regression object:
print(regr.coef_) #value: [0.00755095 0.00780526]

# Result explained: If the "weight" increase by 1kg, the "CO2" emissions will increase by 0.00755095 g. And if the "volume" increase by 1cm3, the "CO2" emissions will increase by 0.00780526 g.


## Let test the model:
#e.g. Increase the "weight" with 1000kg:
predictCO2 = regr.predict([[2300+1000, 1300]])
print(predictCO2) #value: [114.75968007]

# Result explained: A car with 1.3 liter engine and a weight of 3300 kg, will release approximately 115 grams of CO2 for each km it drives.

# Which shows that the coefficient of 0.00755095 is correct:
confirm = 107.2087328 + (0.00755095 * 1000)
print(confirm) #value: 114.75968007
