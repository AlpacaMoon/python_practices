from numpy import format_float_scientific
import pandas as pd
import matplotlib.pyplot as plt
from pandas.io.parsers import read_csv

# Pt 1
# df = pd.read_csv('datasets/world-happiness-report-2021.csv')
# #df['Date'] = pd.to_datetime(df['Date'])
# sea_df = df[ df['Regional indicator'] == 'Southeast Asia' ]
# sea_df.set_index('Country name', inplace=True)
# # '''
# # df = df.set_index('Country name')
# # AND 
# # df.set_index('Country name, inplace=True)
# # DOES THE SAME THING
# # '''
# sea_df.plot()
# df.plot('Country name', 'Ladder score')
# plt.grid(True)
# plt.show()



# #pt 2
df = pd.read_csv('datasets/avocado-prices.csv')
graph_df = pd.DataFrame()
df = df.copy()[ df['type'] == 'organic' ]
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values(by='Date', ascending=True, inplace=True)

for region in df['region'].unique():
    print(region)
    region_df = df.copy()[ df['region'] == region ]
    region_df.set_index('Date', inplace=True)
    region_df.sort_index(inplace=True)
    region_df[f'{region}_AdjAvgPrice'] = region_df['AveragePrice'].rolling(25).mean()

    if graph_df.empty:
        graph_df = region_df[[f'{region}_AdjAvgPrice']]
    else:
        graph_df = graph_df.join(region_df[f'{region}_AdjAvgPrice'])

print(graph_df)

graph_df.dropna().plot(legend=False)

plt.show()