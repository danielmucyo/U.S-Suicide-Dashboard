#Import Libraries
import numpy as np
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objs as go

#Read data and groupby
df=pd.read_csv('c:\\users\\hp\\Documents\\Dashcsv\\Suicide_data.csv')
df=df.groupby(['Year','Sex','Age'],as_index=False)[['Suicides/100k pop','Suicides_no']].sum()

app=dash.Dash(__name__)

#Dash component
app.layout = html.Div([
    html.Div([
        #Y-axis categories dropdown
        html.Label(['Y-axis categories to compare']),
        dcc.Dropdown(
            id='my_dropdown1',
            options=[{'label':'Suicides/100k pop','value':'Suicides/100k pop'},
                     {'label':'Suicides_no','value':'Suicides_no'}
                     
                     ],
             value='Suicides/100k pop',
            multi=False,
            clearable=False,
            style={'width':'50%'}
          ),
        
        #X-axis categories dropdown
        html.Label(['X-axis categories to compare']),
        dcc.Dropdown(
            id='my_dropdown',
            options=[{'label':'Sex', 'value':'Sex'},
                     {'label':'Age','value':'Age'},
                     {'label':'Year','value':'Year'}
                   
                ],
            value='Sex',
            multi=False,
            clearable=False,
            style={'width':'50%'}
            ),
        #Graph
        ]),
    html.Div([
        dcc.Graph(id='the_graph')
        ]),
      
    ])

#Callback
@app.callback(
    Output(component_id='the_graph',component_property='figure'),
    [Input(component_id='my_dropdown1',component_property='value'),
     Input(component_id='my_dropdown',component_property='value')]

    )

def update_graph(my_dropdown1,my_dropdown):
    dff=df
    
    #create bar chart
    barchart=px.bar(data_frame=dff,y=my_dropdown1, x=my_dropdown,color='Sex',
                    opacity=0.95, orientation='v', barmode='group', 
                    title='U.S Suicide Data Interactive Dashboard' )    
    
    barchart.update_layout(xaxis={'categoryorder':'total ascending'},
                           title={'xanchor':'center', 'yanchor': 'top', 'y':0.9,'x':0.5,})

    return(barchart)


if __name__ == '__main__':
    app.run_server()



