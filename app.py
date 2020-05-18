import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
server = app.server


app.layout = html.Div(
    html.Div(
        html.H1(children='My Dashboard')
)


if __name__ == '__main__':
    app.run_server()
