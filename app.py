import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px
df = pd.read_csv("data/formatted_output.csv")
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

df = df.sort_values("Date")
fig = px.line(
    df,
    x="Date",
    y="Sales",
    title="Pink Morsels Sales Over Time",
    labels={
        "Date": "Date",
        "Sales": "Total Sales"
    }
)
app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1("Pink Morsels Sales Visualiser"),
        dcc.Graph(figure=fig)
    ]
)
if __name__ == "__main__":
    app.run(debug=True)

