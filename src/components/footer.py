from dash import html


footer = html.Div(
        className="social-media-icons",
        style = {'text-align':'center'},
        children=[
            html.A(
                href="https://www.linkedin.com/in/vallacheruvu/",
                className="social-icon linkedin",
                target='_blank'
            ),
            html.A(
                href="https://github.com/littlechepa",
                className="social-icon github",
                target='_blank'
            ),
            html.A(
                href="https://www.facebook.com/venkisreevani",
                className="social-icon facebook",
                target='_blank'
            ),
            html.A(
                href="https://www.twitter.com/vallacheruvu",
                className="social-icon twitter",
                target='_blank'
            )                        
        ]
    )