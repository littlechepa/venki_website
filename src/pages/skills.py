from dash import html, dcc
import dash
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc


dash.register_page(__name__, path = "/skills", name = "Skills", order = 3)

skills = ["Python","R Programming","Machine Learning","Deep Learning","Time Series Analysis","Flask","Dash","Shiny","SQL","Predictive Modelling","Forecasting","Docker","RESTful API","Azure","PySpark","Statistics","Snowflake","Data Visualization","Transfer Learning","Dashboard Development"]

layout = dbc.Container(
    [
        # html.Div(
        #     children=[
        #         html.Div("Python", className = "skill-box"),
        #         html.Div("R Programming", className = "skill-box"),
        #         html.Div("Machine Learning", className = "skill-box"),
        #         html.Div("Deep Learning", className = "skill-box"),
        #         html.Div("Time Series Analysis", className = "skill-box"),
        #         html.Div("Flask", className = "skill-box"),
        #         html.Div("Dash", className = "skill-box"),
        #         html.Div("Shiny", className = "skill-box"),
        #         html.Div("SQL", className = "skill-box"),
        #         html.Div("Predictive Modelling", className = "skill-box"),
        #         html.Div("Foreasting", className = "skill-box"),
        #         html.Div("Docker", className = "skill-box"),
        #         html.Div("RESTful API", className = "skill-box"),
        #         html.Div("Azure", className = "skill-box"),
        #         html.Div("Statistics", className = "skill-box"),
        #         html.Div("Snowflake", className = "skill-box"),
        #         html.Div("Data Visualisation", className = "skill-box"),
        #         html.Div("Transfer Learning", className = "skill-box"),
        #         html.Div("Dashboard Development", className = "skill-box")
        #     ]
        # )
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Span(skill, className='skill') for skill in skills
                    ],
                    className = 'skill-container'
                )
            ],
            className = 'skills-container'
        )
    ]
)