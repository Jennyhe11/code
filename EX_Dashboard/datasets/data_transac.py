# this is the data file
import pandas as pd
df = pd.read_excel(r'C:\Users\Administrator\MyProject_Presentation\DashPivottable\pivottable_multipage\src\datasets\transac_summary.xlsx',index_col = 0)

df['Year'] = df.index.year
df['Month'] = df.index.month
cols = ['Year', 'Month','month_revenue', 'refund_rate', 'selling_fees_rate', 'fba_fees_rate',
       'ads_rate', 'rebates_rate', 'other_cost_rate', 'total_cost_rate',
       'gross_rate']
df = df[cols]

column_list = df.columns.tolist()
data = df.values.tolist()
data.insert(0,column_list)
