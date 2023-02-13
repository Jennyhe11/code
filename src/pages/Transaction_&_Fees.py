# this is the dash_pivottable file
import dash
import dash_pivottable
from dash import Input, Output, html,callback
import pandas as pd
import pathlib

dash.register_page(__name__)

PATH = pathlib.Path(__file__).parent
Data_PATH = PATH.joinpath("../datasets").resolve()
df = pd.read_excel(Data_PATH.joinpath("transac_rate.xlsx"),index_col = 0)
df['Year'] = df.index.year
df['Month'] = df.index.month
cols = ['Year', 'Month','month_revenue', 'refund_rate', 'selling_fees_rate', 'fba_fees_rate',
       'ads_rate', 'rebates_rate', 'other_cost_rate', 'total_cost_rate',
       'gross_rate']
df = df[cols]
column_list = df.columns.tolist()
data = df.values.tolist()
data.insert(0,column_list)

layout = html.Div([
    dash_pivottable.PivotTable(
        id='table1',
        data=data,
        cols=['Month'],
        colOrder="key_a_to_z",
        rows=['Year'],
        rowOrder="key_a_to_z",
        rendererName="Grouped Column Chart",
        aggregatorName="Sum",
        vals=["month_revenue"]
    ),
    html.Div(
        id='output1'
    )
])

@callback(
    Output('output1', 'children'),
    [Input('table1', 'cols'),
    Input('table1', 'rows'),
    Input('table1', 'rowOrder'),
    Input('table1', 'colOrder'),
    Input('table1', 'aggregatorName'),
    Input('table1', 'rendererName')])
    
def display_props(cols, rows, row_order, col_order, aggregator, renderer):
    return [
        html.P(str(cols), id='columns'),
        html.P(str(rows), id='rows'),
        html.P(str(row_order), id='row_order'),
        html.P(str(col_order), id='col_order'),
        html.P(str(aggregator), id='aggregator'),
        html.P(str(renderer), id='renderer'),
    ]
