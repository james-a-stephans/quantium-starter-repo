from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

FILE_PATH = './output_file.csv'

#Initialize Dash app.
app = Dash(__name__)

#Read the csv file into a pandas DataFrame and sort by date.
df = pd.read_csv(FILE_PATH)
df.sort_values('date')

#Establish the layout for the graph display, including the header and radio buttons.
app.layout = html.Div(children=[
    html.H1(children='Graph of Pink Morsel Sale Revenue'),

    dcc.Graph(
        id='sales-graph',
        className='graph-sales'
    ),

    dcc.RadioItems(['All', 'North', 'South', 'East', 'West'], 'All', inline=True, id="region", className="options"),
]),


#Determine which region to display sales data from.
@callback(
    Output(component_id='sales-graph', component_property='figure'),
    Input(component_id='region', component_property='value')
)
def change_region(input_value):
    if(input_value == 'All'):
        return px.line(
            df, x='date', y='sales', labels={'date': 'Date', 'sales': 'Sale Revenue in USD'}, title='Total Pink Morsel Sales'
        )
    elif(input_value == 'North'):
        return px.line(
            df.loc[df['region'] == 'north'], x='date', y='sales', labels={'date': 'Date', 'sales': 'Sale Revenue in USD'},
            title='Pink Morsel Sales in the North Region'
        )
    elif(input_value == 'South'):
        return px.line(
            df.loc[df['region'] == 'south'], x='date', y='sales', labels={'date': 'Date', 'sales': 'Sale Revenue in USD'},
            title='Pink Morsel Sales in the South Region'
        )
    elif(input_value == 'East'):
        return px.line(
            df.loc[df['region'] == 'east'], x='date', y='sales', labels={'date': 'Date', 'sales': 'Sale Revenue in USD'},
            title='Pink Morsel Sales in the East Region'
        )
    elif(input_value == 'West'):
        return px.line(
            df.loc[df['region'] == 'west'], x='date', y='sales', labels={'date': 'Date', 'sales': 'Sale Revenue in USD'},
            title='Pink Morsel Sales in the East Region'
        )


#Run the Dash app if this file was called by Python directly.
if __name__ == '__main__':
    app.run_server()