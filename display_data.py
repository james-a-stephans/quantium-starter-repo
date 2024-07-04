from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

FILE_PATH = "./output_file.csv"

#Initialize Dash app.
app = Dash(__name__)

#Read the csv file into a pandas DataFrame and sort by date.
df = pd.read_csv(FILE_PATH)
df.sort_values("date")

#Create the line chart.
fig = px.line(df, x="date", y="sales", labels={"date": "Date", "sales": "Sale Revenue in USD"}, title="Pink Morsel Sales")

#Display the line chart and header in the app.
app.layout = html.Div(children=[
    html.H1(children='Graph of Pink Morsel Sale Revenue'),

    dcc.Graph(
        id='sales-graph',
        figure=fig
    )
])

#Run the Dash app if this file was called by Python directly.
if __name__ == '__main__':
    app.run_server()