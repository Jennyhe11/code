import pandas as pd
df = pd.read_excel(r"C:\Users\Administrator\MyProject_Presentation\DashPivottable\pivottable_multipage\src\datasets\cleaned_campaign_data.xlsx",index_col = 'Month')

df['Year'] = df.index.year
df['Month'] = df.index.month

cols = ['Year','Month','Type', 'Portfolio', 'Orders', 'Sales', 'Spend', 'Im', 'Clicks']
df = df[cols]

column_list = df.columns.tolist()
data = df.values.tolist()
data.insert(0,column_list)