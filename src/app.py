__author__ = "Venkateswarlu Allacheruvu"
__copyright__ = "Copyright 2023, Venki"
__credits__ = ["Venkateswarlu"]
__license__ = "Owned by Venkateswarlu"
__version__ = "1.0"
__maintainer__ = "Venkateswarlu"
__emai__ = "vallacheruvu@gmail.com"
__status__ = "Development"

import sys
from dash import Dash, html, dcc,dash_table, callback, Input, Output, State, ctx
import dash
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
from utils.util_func import print_line_info
from components.navbar import navbar
from components.footer import footer


external_stylesheets = [dbc.themes.BOOTSTRAP, 'https://use.fontawesome.com/releases/v6.4.0/css/all.css']
app = Dash(__name__, use_pages = True, external_stylesheets = external_stylesheets)
app.config.suppress_callback_exceptions = True


app.layout = dbc.Container(
    [
        dbc.Row(
            [
                navbar
            ]
        ),
        dbc.Row(
            [
                dash.page_container                
            ], 
            className = 'page-container'
        ),
        dbc.Row(
            [
                footer
            ],
            className = 'footer'
        )
    ],
    className='wrapper'
)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "development":
            app.run_server(debug = True, port = 8050, use_reloader = True)
        else:
            app.run_server(host = "0.0.0.0", port = 8050)
    else:
        app.run_server(host = "0.0.0.0", port = 8050)




