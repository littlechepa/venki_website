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
print(os.getcwd())
@callback(
    Output("div-cert", "children"),
    Input("div-cert", "children")
)
def render_certs(value):
    folder_path = os.path.join(os.getcwd(), "src/assets/certificates")
    cert_children = []
    for file_name in os.listdir(folder_path):
        cert_children.append(html.Img(src = f"assets/certificates/{file_name}", className = "cert-img"))
    return cert_children

