import os
from dash import html, dcc, callback, Input, Output
import dash
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
# from utils.util_func import render_certificate

dash.register_page(__name__, path = "/certifications", name = "Certifications", order = 5)

layout = dbc.Container(
    [
        html.Div(id = "div-cert"),
    ]
)

@callback(
    Output("div-cert", "children"),
    Input("div-cert", "children")
)
def render_certs(value):
    folder_path = os.path.join(os.getcwd(), "src/assets/certificates")
    cert_children = []

    return cert_children