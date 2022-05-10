import pandas as pd

myDataSet = {
  'cars': ['Honda', 'Toyota', 'Ford'],
  'passings': [3, 5, 7]
}

myVar = pd.DataFrame(myDataSet)
print(myVar)

# Pandas version
print(pd.__version__)
