from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

#Initialize Dash app.
app = Dash(__name__)

#Read the csv file into a pandas DataFrame and sort by date.
df = pd.read_csv("./output_file.csv")
df.sort_values("date")

#Create the line chart.
fig = px.line(df, x="date", y="sales", labels={"date": "Date", "sales": "Sale Revenue in USD"})

#Display the line chart and header in the app.
app.layout = html.Div(children=[
    html.H1(children='Graph of By-Day Sale Revenue from February 6th, 2018 to February 14th, 2022'),

    dcc.Graph(
        id='sales-graph',
        figure=fig
    )
])

#Run the Dash app if this file was called by Python directly.
if __name__ == '__main__':
    app.run()