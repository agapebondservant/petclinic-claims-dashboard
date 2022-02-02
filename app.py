import dash
import dash_core_components as dcc
import dash_html_components as html
import base64
import dash_bootstrap_components as dbc
import plotly.express as px
import sys
import requests
import pandas as pd
import numpy as np
import os


app = dash.Dash()


def refresh_heatmap():
    url = f'https://gemfire1-dev-api.{os.environ['SESSION_NAMESPACE']}.svc.cluster.local:7070/gemfire-api/v1/queries/adhoc'
    r = requests.get(url, params = {"q": "select count(id),city from /claims group by city"})
    response = r.json() 
    # response = [{"id":36,"city":"Indianapolis"},{"id":38,"city":"Fort Worth"},{"id":36,"city":"Columbus"},{"id":37,"city":"Seattle"},{"id":43,"city":"San Jose"},{"id":45,"city":"San Francisco"},{"id":41,"city":"Charlotte"},{"id":60,"city":"Jacksonville"},{"id":35,"city":"Los Angeles"},{"id":50,"city":"San Diego"},{"id":33,"city":"Dallas"},{"id":38,"city":"San Antonio"},{"id":52,"city":"Philadelphia"},{"id":34,"city":"Washington"},{"id":48,"city":"Phoenix"},{"id":37,"city":"Houston"},{"id":47,"city":"Denver"},{"id":44,"city":"New York"},{"id":48,"city":"Austin"},{"id":44,"city":"Chicago"}]
    df = pd.DataFrame(data=sorted(response,key=lambda x: x["id"], reverse=True))
    df = df.head(5)
    df = df.pivot_table(values=df[['id']], columns='city', aggfunc=np.sum)
    figure = px.imshow(df)
    return figure

app.layout = html.Div(style={
    'background': '#505050',
    'color': '#34302d',
    'font-family': 'Arial',
    'margin': '0',
    'height' : '800px'
},children=[
    dbc.Row([
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H1(
                        children='Petclinic Claims',
                        style={
                            'textAlign': 'center',
                            'background': '#34302d',
                            'color': '#6db33f',
                            'margin': '0'
                        }
                    ),
                    #html.Img(src='data:image/png;base64,{}'.format(pets_encoded_image)),
                    html.Div(children='Top 5 Cities with Claims', style={
                        'textAlign': 'center',
                        'fontFamily': 'cursive',
                        'background': '#505050',
                        'color': '#6db33f' 
                    }),
                    html.Label(children='Updating...',style={'margin-top': '10px', 'text-align':'right', 'background': '#505050', 'color': '#6db33f'}),
                    html.Div(style={
                            'margin-top' : '10px',
                            'padding' : '10px',
                            'background': '#505050'
                        }, children=[
                        dcc.Graph(id="graph1", figure=refresh_heatmap()),
                        html.Br()
                    ])
                ])
            )]
        )   
    ])
])

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", debug=True)