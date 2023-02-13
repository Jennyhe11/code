import dash
import dash_pivottable
from dash import Input, Output, html,callback
import pandas as pd
import pathlib


dash.register_page(__name__)

PATH = pathlib.Path(__file__).parent
Data_PATH = PATH.joinpath("../datasets").resolve()
df = pd.read_excel(Data_PATH.joinpath("cleaned_campaign_data.xlsx"),index_col = 'Month')
df['Year'] = df.index.year
df['Month'] = df.index.month
cols = ['Year','Month','Type', 'Portfolio', 'Orders', 'Sales', 'Spend', 'Im', 'Clicks']
df = df[cols]
column_list = df.columns.tolist()
data = df.values.tolist()
data.insert(0,column_list)


layout = html.Div([
    dash_pivottable.PivotTable(
        id='table6',
        data=data,
        cols=['Month'],
        colOrder="key_a_to_z",
        rows=['Portfolio'],
        rowOrder="key_a_to_z",
        rendererName="Grouped Column Chart",
        aggregatorName="Sum",
        vals=["Sales"]
    ),
    html.Div(
        id='output6'
    )
])

@callback(
    Output('output6', 'children'),
    [Input('table6', 'cols'),
    Input('table6', 'rows'),
    Input('table6', 'rowOrder'),
    Input('table6', 'colOrder'),
    Input('table6', 'aggregatorName'),
    Input('table6', 'rendererName')])
    
def display_props(cols, rows, row_order, col_order, aggregator, renderer):
    return [
        html.P(str(cols), id='columns'),
        html.P(str(rows), id='rows'),
        html.P(str(row_order), id='row_order'),
        html.P(str(col_order), id='col_order'),
        html.P(str(aggregator), id='aggregator'),
        html.P(str(renderer), id='renderer'),
    ]

