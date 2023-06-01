from dash import html, dcc
import dash
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc


dash.register_page(__name__, path = "/education", name = "Education", order = 4)

masters_card_content = [
    dbc.CardHeader("Master's"),
    dbc.CardBody(
        [
            html.H5("Post Graduation Diploma in Management(MBA)", className="card-title"),
            html.P(
                "New Delhi Institute of Management, New Delhi, India",
                className="card-text",
            ),
            html.P(
                "05/2015 - 04/2017"
            )
        ]
    ),
]

bachelors_card_content = [
    dbc.CardHeader("Bachelor's"),
    dbc.CardBody(
        [
            html.H5("B.Com(Computers)", className="card-title"),
            html.P(
                "Acharya Nagarjuna University CDE, Guntur, India",
                className="card-text",
            ),
            html.P(
                "06/2008 - 12/2013"
            )
        ]
    ),
]

layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(dbc.Card(masters_card_content, color="primary", outline=True)),
                dbc.Col(dbc.Card(bachelors_card_content, color="secondary", outline=True))
            ],
            className="mb-4",
        )
    ]
)