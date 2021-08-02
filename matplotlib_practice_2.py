import matplotlib.pyplot as plt
import time

def calc_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('Time taken by', func.__name__, end-start)
    return inner


# Import from file #1
# import csv
# x = []
# y = []
# with open('matplotlib practice 2.txt', 'r') as csvfile:
#     plots = csv.reader(csvfile, delimiter=',')
#     for row in plots:
#         x.append(int(row[0]))
#         y.append(int(row[1]))
# plt.plot(x, y, label='Loaded from file!')



# Import from file #2
# import numpy as np
# x, y = np.loadtxt('matplotlib practice 2.txt', delimiter=',', unpack=True)
# plt.plot(x, y, label='Loaded from file!')



# Import from internet
# import urllib.request
# import numpy as np
# import matplotlib.dates as mdates
# url = 'https://pythonprogramming.net/yahoo_finance_replacement'
# source_code = urllib.request.urlopen(url).read().decode()

# data = []
# for line in source_code.split('\n'):
#     if 'Date' not in line and len(line.split(',')) == 7:
#         data.append(line)

# date, openp, highp, lowp, closep, adj_closep, volume = np.loadtxt(  data, 
#                                                                     delimiter=',', 
#                                                                     unpack=True, 
#                                                                     converters={0: lambda x: mdates.datestr2num(x.decode('utf-8'))})

# plt.plot_date(date, closep, '-', label='Price') # The '-' changes the dot-graph into a line-graph



# Basic customization + rotating labels
import urllib.request, numpy as np, matplotlib.dates as mdates

fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))

url = 'https://pythonprogramming.net/yahoo_finance_replacement'
source_code = urllib.request.urlopen(url).read().decode()
data = []
for line in source_code.split('\n'):
    if 'Date' not in line and len(line.split(',')) == 7:
        data.append(line)
date, openp, highp, lowp, closep, adj_closep, volume = np.loadtxt(  data, 
                                                                    delimiter=',', 
                                                                    unpack=True, 
                                                                    converters={0: lambda x: mdates.datestr2num(x.decode('utf-8'))})
ax1.plot_date(date, closep, '-', label='Price') # The '-' changes the dot-graph into a line-graph

for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(45)
ax1.grid(True, color='g', linewidth=0.25)

plt.subplots_adjust(bottom=0.16)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Some Random Graph')
plt.legend()
plt.show()