import dash
import dash_pivottable
from dash import Dash, Input, Output, html,callback
import pathlib
import pandas as pd
import numpy as np

dash.register_page(__name__)

PATH = pathlib.Path(__file__).parent
Data_PATH = PATH.joinpath("../datasets").resolve()
Asin_Report = pd.read_excel(Data_PATH.joinpath("Asin_Report.xlsx"),index_col = 'Month')
Asin_Report['Year'] = Asin_Report.index.year
Asin_Report['Month'] = Asin_Report.index.month
cols = ['Year','Month','Product', 'Sessions', 'Items', 'Units', 'Sales','Convert']
Asin_Report = Asin_Report[cols]

Asin_Report.replace([np.inf, -np.inf], np.nan, inplace=True)
Asin_Report.fillna(0,inplace = True)

columns_list = Asin_Report.columns.tolist()
data =  Asin_Report.values.tolist()
data.insert(0,columns_list)

layout = html.Div([
    dash_pivottable.PivotTable(
        id='table7',
        data=data,
        cols=['Month'],
        colOrder="key_a_to_z",
        rows=['Year'],
        rowOrder="key_a_to_z",
        rendererName="Table Heatmap",
        aggregatorName="Sum",
        vals=["Sessions"]
    ),
    html.Div(
        id='output7'
    )
])

@callback(Output('output7', 'children'),
              [Input('table7', 'cols'),
               Input('table7', 'rows'),
               Input('table7', 'rowOrder'),
               Input('table7', 'colOrder'),
               Input('table7', 'aggregatorName'),
               Input('table7', 'rendererName')])
def display_props(cols, rows, row_order, col_order, aggregator, renderer):
    return [
        html.P(str(cols), id='columns'),
        html.P(str(rows), id='rows'),
        html.P(str(row_order), id='row_order'),
        html.P(str(col_order), id='col_order'),
        html.P(str(aggregator), id='aggregator'),
        html.P(str(renderer), id='renderer'),
    ]


if __name__ == '__main__':
    app.run_server(debug=True)