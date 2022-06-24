# Decision Tree is a flow chart, and can help you make decisions based on previous experience.

#e.g. A person will try to decide if he/she should go to a comedy show or not.

import pandas as pd 
from sklearn import tree 
import pydotplus # for visualization
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt 
import matplotlib.image as pltimg

df = pd.read_csv('shows.csv')
# print(df)

#Change strings values into numerical values:
d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)
# print(df)

#Separate the "feature" columns from the "target" column:
features = ['Age', 'Experience', 'Rank', 'Nationality']
X = df[features]
y = df['Go']
# print(X)
# print(y)

#Create the "decision tree", fit it with our details, and save a ".png" file on the computer:
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('dtree.png') # save the file

img = pltimg.imread('dtree.png')  # read the file
# imgplot = plt.imshow(img)
plt.imshow(img) # show the file
plt.show()
