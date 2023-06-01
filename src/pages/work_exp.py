from dash import html, dcc
import dash
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc


dash.register_page(__name__, path = "/work_exp", name = "Work", order = 2)

layout = dbc.Container(
    [
        html.Div(
            [            
                dbc.Card(
                    dbc.CardBody(
                        [                    
                            html.H4("Specialist Data Scientist", className="card-title"),
                            html.H5("ValueLabs Hyderabad, India", className="card-subtitle"),
                            html.H6("06/2021 - Present", className="card-subtitle"),
                            html.Br(),
                            html.Ul(
                                children=[
                                    html.Li("Built pricing models using ML algorithms"),
                                    html.Li("Modeled the switching behavior of consumers"),
                                    html.Li("Handled end-to-end design and development of dashboards and simulators using Plotly Dash and provided Dash expert support"),
                                    html.Li("Built assortment simulator to have an overview on product mix and gauges the impact on market if any existing product is removed or any new product is added to the market"),
                                    html.Li("Built pricing simulator that helped business teams to test different pricing scenarios before making pricing strategies and downloads the pricing recommendations"),
                                    html.Li("Proposed data science and ML solutions & strategies for various business challenges")
                                ]
                            )
                        ]
                    ),
                    style={"margin": "20px"},
                ),
                dbc.Card(
                    dbc.CardBody(
                        [                    
                            html.H4("Data Scientist", className="card-title"),
                            html.H5("Athena Global Technologies Hyderabad, India", className="card-subtitle"),
                            html.H6("05/2018 - 05/2021", className="card-subtitle"),
                            html.Br(),
                            html.Ul(
                                children=[
                                    html.Li("Undertaking data collection, preprocessing, and building data science models to address business problems"),
                                    html.Li("Built predictive models using machine-learning algorithms and combined models through ensembling"),
                                    html.Li("Automated the sales forecasting that helped to manage inventory, increased stock availability by 95% while reducing the over stocking"),
                                    html.Li("Created dashboards using Shiny and Dash web frameworks"),
                                    html.Li("Identify valuable data sources and automate collection processes, undertake to preprocess structured and unstructured data, and analyze large amounts of information to discover trends and patterns"),
                                ]
                            )
                        ]
                    ),
                    style={"margin": "20px"},
                ),
                dbc.Card(
                    dbc.CardBody(
                        [                    
                            html.H4("Signal Man", className="card-title"),
                            html.H5("Indian Army New Delhi, India", className="card-subtitle"),
                            html.H6("03/2004 - 11/2014", className="card-subtitle"),
                            html.Br(),
                            html.Ul(
                                children=[
                                    html.Li("In-charge of managing and supervising communication center"),
                                    html.Li("Served in UNMIS as a peace keeping soldier"),
                                    html.Li("Computer faculty at technical training establishments"),
                                ]
                            )
                        ]
                    ),
                    style={"margin": "20px"},
                ),
            ],
            className = "work-container"
        )
    ]
)