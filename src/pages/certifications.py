from dash import html, dcc
import dash
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc


dash.register_page(__name__, path = "/certifications", name = "Certifications", order = 5)

layout = dbc.Container(
    [
        html.H1("hello")
    ]
)