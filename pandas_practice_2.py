#groupby
import pandas as pd
from pandas.core.groupby.groupby import GroupByPlot

df = pd.read_csv('datasets/Minimum Wage Data.csv')
smw = pd.DataFrame()

for state, group_data in df.groupby('State'):
    new = group_data.set_index('Year')[['State.Minimum.Wage']].rename(columns={ 'State.Minimum.Wage': state })
    if smw.empty:
        smw = new
    else:
        smw = smw.join(new)

# print(smw)
# print(smw.describe())
# print(smw.corr())

# print((df[ df['State.Minimum.Wage'] == 0 ])['State'].unique())

import numpy as np
# print(smw.replace(0, np.NaN).dropna(axis=1))
print(smw.replace(0, np.NaN).dropna(axis=1).corr())

issue_df = df[ df['State.Minimum.Wage'] == 0 ]
grouped_issues = issue_df.groupby('State')
for state, data in grouped_issues:
    if data['State.Minimum.Wage'].sum() != 0:
        print(state, 'is gucci. ')