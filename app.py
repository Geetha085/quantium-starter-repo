import pandas as pd
from dash import Dash, dcc, html,Input, Output
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
    style={
        "fontFamily": "Arial",
        "backgroundColor": "#f5f5f5",
        "padding": "30px"
    },
    children=[
        html.H1(
            "Pink Morsels Sales Visualiser",
            style={
                "textAlign": "center",
                "color": "#333"
            }
        ),

        html.Div(
            style={
                "width": "50%",
                "margin": "20px auto",
                "textAlign": "center"
            },
            children=[
                html.Label(
                    "Select Region:",
                    style={"fontWeight": "bold"}
                ),
                dcc.RadioItems(
                    id="region-radio",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    style={"marginTop": "10px"}
                ),
            ]
        ),

        html.Div(
            style={
                "backgroundColor": "white",
                "padding": "20px",
                "borderRadius": "8px"
            },
            children=[
                dcc.Graph(id="sales-line-chart")
            ]
        )
    ]
)
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-radio", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        labels={
            "Date": "Date",
            "Sales": "Total Sales"
        },
        title="Pink Morsels Sales Over Time"
    )

    price_increase_date = pd.to_datetime("2021-01-15")

    fig.add_shape(
    type="line",
    x0=price_increase_date,
    x1=price_increase_date,
    y0=filtered_df["Sales"].min(),
    y1=filtered_df["Sales"].max(),
    line=dict(color="red", dash="dash")
    )

    fig.add_annotation(
    x=price_increase_date,
    y=filtered_df["Sales"].max(),
    text="Price Increase",
    showarrow=True,
    arrowhead=1
    )
    return fig

if __name__ == "__main__":
    app.run(debug=True)

