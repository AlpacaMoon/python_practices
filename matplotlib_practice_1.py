import matplotlib.pyplot as plt
import random


# Linear Graph
# x1 = [1,2,3,4,5]
# y1 = [6,8,3,4,6]
# x2 = [1,2,3,4,5]
# y2 = [10,6,7,4,4]
# plt.plot(x1, y1, label='First')
# plt.plot(x2, y2, label='Second')


# Bar chart
# x = [2,4,6,8,10]
# y = [1,6,4,5,3]
# x2 = [1,3,5,7,9]
# y2 = [5,4,8,3,2]
# plt.bar(x, y, label='Bar1', color='r')
# plt.bar(x2, y2, label='Bar2')


# Histogram
# ages = [random.randrange(1, 120) for _ in range(100)]
# bins = [i*10 for i in range(13)]
# print(bins)
# plt.hist(ages, bins, histtype='bar', rwidth=0.8)


# Scatter Plot
# x=[random.randrange(0,100) for i in range(100)]
# y=[random.randrange(0,100) for _ in range(100)]
# plt.scatter(x, y, label='scat', color='orange', marker='*', s=1000)


# #Stack Plot
# days = [1,2,3,4,5]

# sleeping =[7, 8, 6, 11, 7] 
# eating =  [2, 3, 4, 3, 2]
# working = [7, 8, 7, 2, 2]
# playing = [8, 5, 7, 8, 13]

# plt.stackplot(days, sleeping, eating, working, playing, colors=['m', 'c', 'r', 'k'], labels=['sleeping','eating','working','playing '])


# Pie chart
# slices = [8, 2, 9, 5]
# activities = ['sleeping', 'eating', 'working', 'playing']
# plt.pie(slices, labels=activities, startangle=90, shadow=True, explode = (0, 0.1, 0, 0), autopct='%1.1f%%')

plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Some Random Graph')
plt.legend()
plt.show()