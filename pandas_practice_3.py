# Visualizing correlation table
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Group data

df = pd.read_csv('datasets/Minimum Wage Data.csv')
min_wage = pd.DataFrame()
for state, data in df.groupby('State'):
    modified_data = data.set_index('Year')[['State.Minimum.Wage.2020.Dollars']].rename(columns={'State.Minimum.Wage.2020.Dollars': state})
    if min_wage.empty:
        min_wage = modified_data
    else:
        min_wage = min_wage.join(modified_data)
        # OR
        # min_wage = pd.concat([min_wage, modified_data], axis=1)

# Create a correlation table without Na's
min_wage_corr = min_wage.replace(0, np.NaN).dropna(axis=1).corr()

# Customize table into heatmap
labels = [s[:2] for s in min_wage_corr.columns]

fig1 = plt.figure(figsize=(12,12))
ax1 = fig1.add_subplot(111)

ax1.matshow(min_wage_corr, cmap=plt.cm.RdYlGn)

ax1.set_xticks(np.arange(len(labels)))
ax1.set_yticks(np.arange(len(labels)))
ax1.set_xticklabels(labels)
ax1.set_yticklabels(labels)
plt.title('First Graph')
# plt.show()

# Import US Postal codes from internet and convert to csv
# df2 = pd.read_html('https://www.infoplease.com/us/postal-information/state-abbreviations-and-state-postal-codes')
# df2[0].drop('Abbreviation', axis=1, inplace=True)
# df2[0].to_csv('datasets/US State Postal Codes.csv', index=False)


state_df = pd.read_csv('datasets/US State Postal Codes.csv', index_col=0)
postal_dict = state_df['Postal Code'].to_dict()

# Hardcoding states that isnt recorded
postal_dict['Guam'] = 'GU'
postal_dict['Puerto Rico'] = 'PR'
postal_dict['U.S. Virgin Islands'] = 'VI'

labels = [postal_dict[each] for each in min_wage_corr.columns]

fig1 = plt.figure(figsize=(12,12))
ax1 = fig1.add_subplot(111)
ax1.matshow(min_wage_corr, cmap=plt.cm.RdYlGn)
ax1.set_xticks(np.arange(len(labels)))
ax1.set_yticks(np.arange(len(labels)))
ax1.set_xticklabels(labels)
ax1.set_yticklabels(labels)
plt.title('Second Graph')
plt.show()

