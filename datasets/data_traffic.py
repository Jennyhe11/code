import pandas as pd
import numpy as np

Asin_Report = pd.read_excel('Asin_Report.xlsx',index_col = 'Month')

Asin_Report['Year'] = Asin_Report.index.year
Asin_Report['Month'] = Asin_Report.index.month
cols = ['Year','Month','Product', 'Sessions', 'Items', 'Units', 'Sales','Convert']
Asin_Report = Asin_Report[cols]

Asin_Report.replace([np.inf, -np.inf], np.nan, inplace=True)
Asin_Report.fillna(0,inplace = True)

columns_list = Asin_Report.columns.tolist()
data =  Asin_Report.values.tolist()
data.insert(0,columns_list)