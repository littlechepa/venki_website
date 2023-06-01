from dash import html, dcc
import dash
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc


dash.register_page(__name__, path = "/", name = "Venki", order = 1)

layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardImg(
                                src="/assets/images/venki_prf_img.jpg",
                                top=True,
                                className="profile-photo"
                            ),
                            dbc.CardBody(
                                [
                                    html.H4("Venkateswarlu Allacheruvu", className="card-title"),
                                    html.P("Data Scientist", className="card-subtitle"),
                                    
                                ]
                            )
                        ],
                        className="profile-card"
                    ),
                    width = 4
                ),
                dbc.Col(
                    [
                        html.P(
                            [
                                "Highly efficient and innovative professional with 5 years of experience in Data Science & Analytics. Worked with teams to create full-scale data solutions and industry-specific products. Expertise in developing predictive models using appropriate machine learning algorithms. Proficient in Time Series Analysis, Dynamic regression, and Forecasting. Builds best-fit models based on data and provides valuable insights for business problems. Well-versed in analyzing data across various domains. Highly proficient in designing and building dashboards using Python Dash & R Shiny. Possesses excellent project management and interpersonal skills. Enjoys collaborating as a team player and taking on leadership roles. Also serves as an IT faculty at an Indian Army training center. Certified Data Scientist from DataCamp."
                            ],
                            style = {'margin':'20px', 'text-align':'justify'}
                            # className="profile-card"
                        )
                    ]
                )
            ],
            justify="center"
        )
    ],
    fluid=True
)