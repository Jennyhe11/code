import pandas as pd

df = pd.read_excel('cleaned_SPImShare_data.xlsx',index_col = 'Month')

df['Year'] = df.index.year
df['Month'] = df.index.month

cols = ['Year', 'Month','Search', 'Targeting', 'Match', 'Portfolio', 'Clicks', 'Spend',
       'Orders', 'Sales', 'AdGroup']
df = df[cols]

column_list = df.columns.tolist()
data = df.values.tolist()
data.insert(0,column_list)