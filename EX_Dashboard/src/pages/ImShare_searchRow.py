import dash
import dash_pivottable
from dash import Input, Output, html,callback
import pandas as pd
import pathlib

dash.register_page(__name__)

PATH = pathlib.Path(__file__).parent
Data_PATH = PATH.joinpath("../datasets").resolve()
df = pd.read_excel(Data_PATH.joinpath("cleaned_SPImShare_data.xlsx"),index_col = 'Month')
df['Year'] = df.index.year
df['Month'] = df.index.month
cols = ['Year', 'Month','Search', 'Targeting', 'Match', 'Portfolio', 'Clicks', 'Spend',
       'Orders', 'Sales', 'AdGroup']
df = df[cols]
column_list = df.columns.tolist()
data = df.values.tolist()
data.insert(0,column_list)


layout = html.Div([
    dash_pivottable.PivotTable(
        id='table4',
        data=data,
        cols=['Month'],
        colOrder="key_a_to_z",
        rows=['Search'],
        rowOrder="key_a_to_z",
        rendererName="Grouped Column Chart",
        aggregatorName="Sum",
        vals=["Orders"],
        valueFilter={'Orders': {'0': False,'1': False,'2': False}}
    ),
    html.Div(
        id='output4'
    )
])

@callback(Output('output4', 'children'),
              [Input('table4', 'cols'),
               Input('table4', 'rows'),
               Input('table4', 'rowOrder'),
               Input('table4', 'colOrder'),
               Input('table4', 'aggregatorName'),
               Input('table4', 'rendererName')])
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