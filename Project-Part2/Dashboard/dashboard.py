import dash
from dash import dcc, html
import pandas as pd
from dash.dependencies import Input, Output

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ]),
    ], style={'marginLeft': 'auto', 'marginRight': 'auto'})

app = dash.Dash()
app.layout = html.Div(
    children=[
        html.H1(children="Application for companies support", style={'text-align': 'center'}),
        html.P(
            children="Overview on existing applications in the market to manage ADHD and LSD children", style={'text-align': 'center'}
        ),
        html.Div([html.Img(
            src='https://uploads-ssl.webflow.com/5b651f8b5fc94c6f5f470a7a/5fc0cb7e65940121de0373b3_Chaos%20Theory%20Serious%20Games%20Education%20Types%20(1).jpg',
            style={'float': 'left', 'display': 'block', 'width': '400px', 'height': '200px', 'margin-left': '12%',
                   'margin-top': '10%'})]),
        html.Div([dcc.Graph(
            id="example3",
            figure={
                'data': [
                    {'values': [6, 5],
                     'labels': ['ADHD serious games', 'LSD serious games'],
                     'type': 'pie',
                     'name': 'Ships'}
                ],
                'layout': {
                    'title': 'Serious games [11 apps]'
                }
            },
            style={'float': 'right', 'display': 'block', 'margin-right': '5%'}
        )]),
        html.Div(style={'clear': 'both'}),
        html.Div([
            dcc.Dropdown(
                id='demo-dropdown',
                style={'text-align': 'center'},
                options=[
                    {'label': 'Specific learning disorders', 'value': 'LSD'},
                    {'label': 'Attention deficit hyperactivity disorder', 'value': 'ADHD'},
                    {'label': 'Other', 'value': 'Other'}
                ],
                value='None'
            ),
            html.Div(id='dd-output-container')
        ], style={'width': '600px', 'text-align': 'center', 'margin-top': '30px', 'margin-left': 'auto', 'margin-right': 'auto'}),
        html.Div([html.Img(src='https://media.springernature.com/full/springer-cms/rest/v1/content/18319572/data/v2',
                           style={'float': 'left', 'display': 'block', 'width': '15%', 'margin-top': '10%'}),
                  html.Img(src='https://en.library.ipm.edu.mo/sites/default/files/logo_dbs_sciencedirect.jpg',
                           style={'float': 'left', 'display': 'block', 'width': '15%',
                                  'margin-top': '10%'}),
                  html.Img(src='https://bilkentlibrary.files.wordpress.com/2016/03/springer.png',
                           style={'float': 'left', 'display': 'block', 'width': '15%', 'margin-top': '12%'}),
                  html.Img(
                      src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/IEEE_logo.svg/1200px-IEEE_logo.svg.png',
                      style={'float': 'left', 'display': 'block', 'width': '15%', 'margin-top': '15%'}),
                  html.Img(
                      src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Scopus_logo.svg/2560px-Scopus_logo.svg.png',
                      style={'float': 'left', 'display': 'block', 'width': '15%', 'margin-top': '15%'}),
                  html.Img(src='https://eric.ed.gov/img/eric_large.png',
                           style={'float': 'left', 'display': 'block', 'width': '15%', 'margin-top': '14%'})
                  ], style={'width': '45%', 'margin-left': '440px'})

    ]
)


@app.callback(
    Output('dd-output-container', 'children'),
    Input('demo-dropdown', 'value')
)
def update_output(value):
    if value == 'LSD':
        df = pd.read_csv("C:/Users/Public/learning_disorders.csv")
        return (html.Div([
            html.H4(children='Serious games - Specific learning disorders'),
            generate_table(df)
        ]))
    elif value == 'ADHD':
        df = pd.read_csv("C:/Users/Public/attention deficit.csv")
        return (html.Div([
            html.H4(children='Serious games - Attention deficit hyperactivity disorder'),
            generate_table(df)
        ]))
    elif value == 'Other':
        df = pd.read_csv("C:/Users/Public/other.csv")
        return (html.Div([
            html.H4(children='Serious games - Other'),
            generate_table(df),
        ]))


if __name__ == '__main__':
    app.run_server()
