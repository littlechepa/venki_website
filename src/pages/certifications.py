from dash import html, dcc
import dash
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
from utils.util_func import render_certificate

dash.register_page(__name__, path = "/certifications", name = "Certifications", order = 5)

layout = dbc.Container(
    [
        html.Div(
                children = render_certificate()
        )
    ]
)