# Machine learning with scikit-learn
import pandas as pd
import sklearn
from sklearn import svm, preprocessing


df = pd.read_csv('datasets/diamonds.csv', index_col=0)

cut_class_dict = {'Fair': 1, 'Good': 2, 'Very Good': 3, 'Premium': 4, 'Ideal': 5}
color_dict = {'J': 1, 'I': 2, 'H': 3, 'G': 4, 'F': 5, 'E': 6, 'D': 7}
clarity_dict = {'I3': 1, 'I2': 2, 'I1': 3, 'SI2': 4, 'SI1': 5, 'VS2': 6, 'VS1': 7, 'VVS2': 8, 'VVS1': 9, 'IF': 10, 'FL': 11}

df['cut'] = df['cut'].map(cut_class_dict)
df['color'] = df['color'].map(color_dict)
df['clarity'] = df['clarity'].map(clarity_dict)

df = sklearn.utils.shuffle(df)

X = df.drop('price', axis=1).values
X = preprocessing.scale(X)
y = df['price'].values

test_size = 200

X_train = X[:-test_size]
y_train = y[:-test_size]

X_test = X[-test_size:]
y_test = y[-test_size:]

clf = svm.SVR(kernel='linear') # Results may contain nonsense like Model: -3, Actual: 500
# clf = svm.SVR(kernel='rbf') # Result are more logical, but score is worse (eg: linear=0.81, rbf=0.55)

model = clf.fit(X_train, y_train)
print('Model:', model)

res = clf.score(X_test, y_test)
print('Score:', res)

for a, b in zip(X_test, y_test):
    g = clf.predict([a])
    print(f'g: {g}\n Model: {g[0]}, Actual: {b}')

