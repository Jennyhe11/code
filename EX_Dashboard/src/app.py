import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets = [dbc.themes.LUMEN], use_pages = True)
server = app.server

app.layout = html.Div([
        html.H1('EX Dashboard',className="text-primary text-center mt-3"),
        dbc.Nav([
            dbc.NavLink(
                    [html.Div(page['name'])],href = page['path'],active = 'exact'
                    ) for page in dash.page_registry.values()
            ],vertical = False, pills = True,class_name="mb-2 bg-light border shadow-lg"),  
        dbc.Row([
            dbc.Col(
                dash.page_container,width = 8
            )
        ]) 
        
    ])
    

if __name__=='__main__':
    app.run_server(debug = True)
