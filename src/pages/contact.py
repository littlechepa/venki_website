from dash import html, dcc
import dash
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc


dash.register_page(__name__, path = "/contact", name = "Contact", order = 6)

contact_content_mobile = [
    dbc.CardHeader("Mobile"),
    dbc.CardBody(
        [
            html.H5("+919966090437"),
            html.P(
                "India",
                className="card-text",
            ),
            html.P(
                "Available from 09:30 to 1830 IST everyday"
            )
        ]
    ),
]
contact_content_email = [
    dbc.CardHeader("Email"),
    dbc.CardBody(
        [
            html.H5("vallacheruvu@gmail.com")
        ]
    ),
]

layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(dbc.Card(contact_content_mobile, color="primary", outline=True)),
                dbc.Col(dbc.Card(contact_content_email, color="primary", outline=True))
            ],
            className="mb-4",
        )
    ]
)


