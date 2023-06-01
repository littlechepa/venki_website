from dash import html, dcc
import dash
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc


dash.register_page(__name__, path = "/contact", name = "Contact", order = 6)

layout = dbc.Container(
    [
        html.H1("hello")
    ]
)