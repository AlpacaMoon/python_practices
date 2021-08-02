# Combining multiple datasets
import pandas as pd
import numpy as np

min_wage_data_df = pd.read_csv('datasets/Minimum Wage Data.csv')
min_wage_df = pd.DataFrame()
for state, data in min_wage_data_df.groupby('State'):
    col = data.set_index('Year')[['State.Minimum.Wage.2020.Dollars']].rename(columns={'State.Minimum.Wage.2020.Dollars': state})
    if min_wage_df.empty:
        min_wage_df = col
    else:
        min_wage_df = min_wage_df.join(col)
        # OR
        # min_wage_df = pd.concat([min_wage_df, col], axis=1)
min_wage_df = min_wage_df.replace(0, np.NaN).dropna(axis=1)



unemp_county = pd.read_csv('datasets/US Unemployment Rate by County, 1990-2016/output.csv')
unemp_county_2015 = unemp_county.copy()[ (unemp_county['Year']==2015) & (unemp_county['Month']=='February') ]

def get_min_wage(year, state):
    try:
        return min_wage_df.loc[year][state]
    except:
        return np.NaN
unemp_county_2015['min_wage'] = list(map(get_min_wage, unemp_county_2015['Year'], unemp_county_2015['State']))
# print(unemp_county_2015[['Rate', 'min_wage']].corr())
# print(unemp_county_2015[['Rate', 'min_wage']].cov())

us_postal = pd.read_csv('datasets/US State Postal Codes.csv', index_col=0)
postal_dict = us_postal['Postal Code'].to_dict()
unemp_county_2015['State'] = unemp_county_2015['State'].map(postal_dict)



pres16 = pd.read_csv('datasets/US Presidential Election Votes by County, 2016.csv')
pres16 = pres16.copy()[ pres16['cand']=='Donald Trump' ]
pres16.rename(columns={'county': 'County', 'st': 'State'}, inplace=True)

for each in [unemp_county_2015, pres16]:
    each.set_index(['County', 'State'], inplace=True)
pres16 = pres16[['pct']]
pres16.dropna(inplace=True)
pres16.rename(columns={'pct':'Vote %'}, inplace=True)



result = unemp_county_2015.merge(pres16, on=['County', 'State'])
result.dropna(inplace=True)
result.drop('Year', axis=1, inplace=True)

for each in [result, result.corr(), result.cov()]:
    print('Candidate: Donald Trump')
    print(each, '\n')


