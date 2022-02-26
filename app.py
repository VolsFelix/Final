import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd
import dash_bootstrap_components as dbc

# data source: https://www.kaggle.com/yamqwe/largest-us-retailers-2015e
# youtube tutorial https://www.youtube.com/watch?v=ln8dyS2y4Nc

retail = pd.read_csv(r"C:\Users\cole\Documents\Spring MSBA\App Design\archive\Retail.csv")


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


# styling the sidebar layout
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# padding for the page content/links
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Pages", className="display-4"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Sales Count", href="/sales_count", active="exact"),
                dbc.NavLink("Store Count", href="/store_count", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content
])


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return [
                html.H3('Welcome. This web app shows some insights into the top 100 US retailers.',
                        style={'textAlign':'center'}),
                ]
    elif pathname == "/sales_count":
        return [
                html.H1('Sales Count',
                        style={'textAlign':'center'}),
                dcc.Graph(id='bargraph',
                         figure=px.bar(retail, barmode='group', x='Company',
                         y='Sales'))
                ]
    elif pathname == "/store_count":
        return [
                html.H1('Store Count',
                        style={'textAlign':'center'}),
                dcc.Graph(id='bargraph',
                         figure=px.bar(retail, barmode='group', x='Company',
                         y='Stores'))
                ]
   


if __name__=='__main__':
    app.run_server(debug=True, port=3000)