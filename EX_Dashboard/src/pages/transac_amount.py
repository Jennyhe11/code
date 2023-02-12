# this is the dash_pivottable file
import dash
import dash_pivottable
from dash import Input, Output, html,callback
import pandas as pd
import pathlib

dash.register_page(__name__,path='/')

PATH = pathlib.Path(__file__).parent
Data_PATH = PATH.joinpath("../datasets").resolve()
df = pd.read_excel(Data_PATH.joinpath("transac_amount.xlsx"),index_col = 0)
df = df.drop(columns = 'Total_Revenue')
df = df.stack().to_frame()
df = df.reset_index()
df = df.rename(columns = {'level_0':'Date','level_1':'Type',0:'Value'})
df.index = pd.to_datetime(df['Date'])
df['Year'] = df.index.year
df['Month'] = df.index.month
cols = ['Year', 'Month', 'Type','Value']
df = df[cols]
column_list = df.columns.tolist()
data = df.values.tolist()
data.insert(0,column_list)

layout = html.Div([
    dash_pivottable.PivotTable(
        id='table5',
        data=data,
        cols=['Month'],
        colOrder="key_a_to_z",
        rows=['Type'],
        rowOrder="key_a_to_z",
        rendererName="Grouped Column Chart",
        aggregatorName="Sum",
        vals=["Value"]
    ),
    html.Div(
        id='output5'
    )
])

@callback(
    Output('output5', 'children'),
    [Input('table5', 'cols'),
    Input('table5', 'rows'),
    Input('table5', 'rowOrder'),
    Input('table5', 'colOrder'),
    Input('table5', 'aggregatorName'),
    Input('table5', 'rendererName')])
    
def display_props(cols, rows, row_order, col_order, aggregator, renderer):
    return [
        html.P(str(cols), id='columns'),
        html.P(str(rows), id='rows'),
        html.P(str(row_order), id='row_order'),
        html.P(str(col_order), id='col_order'),
        html.P(str(aggregator), id='aggregator'),
        html.P(str(renderer), id='renderer'),
    ]
