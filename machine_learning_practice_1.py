# Machine Learning using Linear Regression

import pandas as pd
import quandl, math, datetime
from sklearn import preprocessing, svm, model_selection
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import pickle


# Import dataset, then extract and create the columns needed for regression
# We use HL_PCT and PCT_change instead of the original data becuz of how regression works
# Linear Regression only takes what you feed it, so it is better to feed informational data
df = quandl.get("EURONEXT/ADYEN", authtoken="25Buo8odmG3-y1eVFFWf")
df = df[['Open', 'High', 'Low', 'Last', 'Volume']].rename(columns={'Last': 'Close'})

df['HL_PCT'] = (df['High'] - df['Low']) / df['Close'] * 100.0
df['PCT_change'] = (df['Close'] - df['Open']) / df['Open'] * 100.0

df = df[['Close', 'HL_PCT', 'PCT_change', 'Volume']]

forecast_col = 'Close'
df.fillna(-99999, inplace=True) # ML can't accept NaN values, so use something like -99999

# Since we want to predict the future stock price, we create a new 'label' for it as the label
# The Close, HL_PCT, PCT_change and Volume will serve as features
forecast_out = math.ceil(0.01 * len(df))
# print(forecast_out)
df['label'] = df[forecast_col].shift(-forecast_out)


# X is the features, X_predict is the features that we want to predict its labels
df_predict = df.copy()
X = np.array(df_predict.drop('label', axis=1))
X = preprocessing.scale(X)
X_train_test = X[:-forecast_out]
X_predict = X[-forecast_out:]

# y is the labels, used in training and testing like X but not X_predict
df_predict.dropna(inplace=True) # Dropped na as those rows are the ones that we want to predict
y_train_test = np.array(df_predict['label'])


# Split into training and testing data
X_train, X_test, y_train, y_test = model_selection.train_test_split(X_train_test, y_train_test, test_size=0.2)

# Building model and saving to file
# clf = LinearRegression() # use n_jobs parameter to indicate the amount of cpus to work with, n_jobs=-1 to use all cpu
# clf.fit(X_train, y_train)
# with open('linear_regression_stocks.pickle', 'wb') as f:
#     pickle.dump(clf, f)

# Import model from file
pickle_in = open('linear_regression_stocks.pickle', 'rb')
clf = pickle.load(pickle_in)
pickle_in.close()

accuracy = clf.score(X_test, y_test)
# print(accuracy)

# Forecasting based on the given features
forecast_res = clf.predict(X_predict)

# This section below is just to assign a new column for the forecasting results and graphing it
last_date = df_predict.iloc[-1].name
last_unix = datetime.datetime.timestamp(last_date)
one_day = 24 * 60 * 60
next_unix = last_unix + one_day
df_predict['Forecast'] = np.NaN # Default as NaN as data before has no forecasting results

for each in forecast_res:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    df_predict.loc[next_date] = [np.NaN for _ in range(len(df_predict.columns) - 1)] + [each]
    next_unix += one_day

style.use('ggplot')
df['Close'].plot()
df_predict['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

