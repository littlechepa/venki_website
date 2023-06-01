import dash_bootstrap_components as dbc
from dash import html


home_icon = html.Div(
    [
        html.I(className = "fa-solid fa-house fa-xl"),
        html.H6("Home")
    ]
)
work_icon = html.Div(
    [
        html.I(className = "fa-solid fa-user-tie fa-xl"),
        html.H6("Work")
    ]
)
skill_icon =  html.Div(
    [
        html.I(className = "fa-solid fa-screwdriver-wrench fa-xl"),
        html.H6("Skills")
    ]
)
edu_icon =  html.Div(
    [
        html.I(className = "fa-solid fa-user-graduate fa-xl"),
        html.H6("Education")
    ]
)
cert_icon =  html.Div(
    [
        html.I(className = "fa-solid fa-certificate fa-xl"),
        html.H6("Certifications")
    ]
)
contact_icon =  html.Div(
    [
        html.I(className = "fa-solid fa-address-book fa-xl"),
        html.H6("Contact")
    ]
)


navbar = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink(home_icon, href = "/", active = "exact", style = {})),
        dbc.NavItem(dbc.NavLink(work_icon, href = "/work_exp", active = "exact", style = {})),
        dbc.NavItem(dbc.NavLink(skill_icon, href = "/skills", active = "exact", style = {})),
        dbc.NavItem(dbc.NavLink(edu_icon, href = "/education", active = "exact", style = {})),
        dbc.NavItem(dbc.NavLink(cert_icon, href = "/certifications", active = "exact", style = {})),
        dbc.NavItem(dbc.NavLink(contact_icon, href = "/contact", active = "exact", style = {}))
    ],
    pills = True,
    fill = True
)

