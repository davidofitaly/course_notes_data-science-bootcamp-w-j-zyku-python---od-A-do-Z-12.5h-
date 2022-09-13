import dash
from dash import Dash, html, dcc
import plotly.graph_objects as go



app = dash.Dash(__name__)

app.layout = html.Div(children=[

    html.H2(children='Hello Dash'),

    dcc.Graph(
        figure = go.Figure(
            go.Bar(
                x = ['2017', '2018', '2019'],
                y = [150, 300, 80],
                name='lokalnie'
            ),
            go.Bar(
                x = ['2017', '2018', '2019'],
                y = [90, 80, 10],
                name='online'
            )
        ])

    )

])

if __name__ == "__main__":
    app.run_server(debug=True)
