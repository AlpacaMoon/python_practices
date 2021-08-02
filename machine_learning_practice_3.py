# K nearest neighbors by sklearn

import pandas as pd
from sklearn import preprocessing, model_selection, neighbors
import numpy as np

df = pd.read_csv("datasets/Breast Cancer Wisconsin (Original) Data Set/breast-cancer-wisconsin.data")
df.replace("?", -99999, inplace=True)
df.drop('id', axis=1, inplace=True)

X = np.array(df.drop('class', 1))
y = np.array(df['class'])

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print("Accuracy:", accuracy)

example_measures = np.array([[2,1,1,1,2,1,1,1,2]])
# example_measures = example_measures.reshape(len(example_measures), -1)  # Dk about this, seems like using example_measures as a 2d array fixes it
prediction = clf.predict(example_measures)

print(prediction)