# Linear Regression - programming the best fit slope algorithm
# y = mx + b
# m = ( (mean_x * mean_y) - mean_xy ) / ( (mean_x)^2 - (mean_(x^2)) )

import numpy as np
from statistics import fmean
from random import randrange
import matplotlib.pyplot as plt


plt.style.use('ggplot')

# *for the xs and ys array:
# mean(np.array) without dtype=np.float64 will cause the result to be truncated, reducing accuracy
# If you want to be sure / dont want to use dtype=np.float64, use fmean instead of mean so that all calculations involved use floats

# xs = np.array([1,2,3,4,5,6], dtype=np.float64)
# ys = np.array([5,4,6,5,6,7], dtype=np.float64)

def create_datasets(n, variance, step=2, correlation=False):
    xs = [i for i in range(n)]
    ys = []
    v = 0
    for _ in range(n):
        y = v + randrange(-variance, variance)
        ys.append(y)
        if correlation and correlation=='pos':
            v += step
        elif correlation and correlation=='neg':
            v -= step
    return np.array(xs, dtype=np.float64), np.array(ys, dtype=np.float64)

def best_fit_slope_and_intercept(xs, ys):
    m = ( (fmean(xs) * fmean(ys)) - fmean(xs*ys) ) / ( (fmean(xs) ** 2 ) - (fmean(xs ** 2)) )
    b = fmean(ys) - (m * fmean(xs))
    return m, b

def squared_error(y_orig, y_line):
    return sum((y_line - y_orig)**2)

# r^2 = 1 - ( (SE of best_fit_y) / (SE of mean_y) )
def coefficient_of_determination(y_orig, y_line):
    return 1 - ( squared_error(y_orig, y_line) / squared_error(y_orig,  fmean(y_orig)) )

xs, ys = create_datasets(100, 50, 2, correlation='pos')
m, b = best_fit_slope_and_intercept(xs, ys)

best_fit_line = [(m*x)+b for x in xs]
r_squared = coefficient_of_determination(ys, best_fit_line)
print(r_squared)


# To predict a value
predict_x = 10
predict_y = (m * predict_x) + b

plt.scatter(xs, ys)
plt.scatter(predict_x, predict_y)
plt.plot(xs, best_fit_line)
plt.show()