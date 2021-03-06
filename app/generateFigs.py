import os
from app.generatePoints import *
import plotly.express as px
import plotly
import pandas as pd
import json
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

curDir = os.path.dirname(__file__)
global_temp_path = os.path.abspath(os.path.join(curDir, "..", "data", "GlobalTemperatures.csv"))
state_temps_path = os.path.abspath(os.path.join(curDir, "..", "data", "GlobalLandTemperaturesByState.csv"))
predict_year = 2050
year1 = 1900
year2 = 2000
years_after = 10


def generate_global_data():
    l_and_o_yearly_data = land_and_ocean_yearly(global_temp_path)
    year_to_temps = l_and_o_yearly_data[0]
    year_to_error = l_and_o_yearly_data[1]
    df = pd.DataFrame(columns=["Year", "Average Global Temperature", "Error"])
    for year in year_to_temps:
        df2 = pd.DataFrame([[year, year_to_temps.get(year), year_to_error.get(year)]],
                           columns=["Year", "Average Global Temperature", "Error"])
        df = df.append(df2)
    fig = px.line(df, x="Year", y="Average Global Temperature", title='Test', error_y="Error")

    pred = generate_regression(df)

    line_obj = fig.data[0]
    line_obj.line.color = "#FF0800"
    line_obj.mode = "lines+markers"
    line_obj.marker = {
        "color": '#4C516D'}
    line_obj.error_y.color = "black"
    line_obj.error_y.thickness = .7
    line_obj.error_y.width = 0
    fig.update_layout(
        title="Global Average Yearly Temperature 1850 - 2015",
        yaxis_title="Global Temperature (" + u"\u2103" + ")"
    )
    data = [fig]

    return [json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder), pred]


def generate_regression(df):
    x = df.iloc[:, 0:1].values
    y = df.iloc[:, 1].values
    poly = PolynomialFeatures(degree=2)
    X_poly = poly.fit_transform(x)
    poly.fit(X_poly, y)
    lin = LinearRegression()
    lin.fit(X_poly, y)
    plt.scatter(x, y, color="#4C516D", s=10)

    plt.plot(x, lin.predict(poly.fit_transform(x)), color="#FF0800")
    plt.title("Global Temperature Regression Model")
    plt.xlabel("Year")
    plt.ylabel("Global Temperature (" + u"\u2103" + ")")

    prediction_val = round(lin.predict(poly.fit_transform([[predict_year]]))[0], 2)

    plt.savefig(os.path.abspath(os.path.join(curDir, "static", "img", "earth_pred.png")))
    return prediction_val


def generate_choropleth_maps():
    state_data = state_average_two_years(year1, year2, years_after, state_temps_path)
    year1_data = state_data[0]
    year2_data = state_data[1]

    df = pd.DataFrame(columns=["State", "Temperature"])
    for state in year1_data:
        df2 = pd.DataFrame([[state, year1_data.get(state)]], columns=["State", "Temperature"])
        df = df.append(df2)
    states = df["State"]
    temps = df["Temperature"]
    fig = px.choropleth(locations=states, locationmode="USA-states", color=temps, scope="usa",
                        color_continuous_scale=["#4197b0", "#ffffad", "#ffcb58", "#e0603f"], range_color=[5, 15],
                        title="Average State Temperatures between " + str(year1) + " and " + str(year1 + years_after),
                        labels={"locations": "State", "color": "Temperature(" + u"\u2103" + ")"})
    fig.update_layout(
        dragmode=False
    )
    data = [fig]

    period1_fig = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    df = pd.DataFrame(columns=["State", "Temperature"])
    for state in year2_data:
        df2 = pd.DataFrame([[state, year2_data.get(state)]], columns=["State", "Temperature"])
        df = df.append(df2)
    states = df["State"]
    temps = df["Temperature"]
    fig = px.choropleth(locations=states, locationmode="USA-states", color=temps, scope="usa",
                        color_continuous_scale=["#4197b0", "#ffffad", "#ffcb58", "#e0603f"], range_color=[5, 15],
                        title="Average State Temperatures between " + str(year2) + " and " + str(year2 + years_after),
                        labels={"locations": "State", "color": "Temperature(" + u"\u2103" + ")"})

    fig.update_layout(
        dragmode=False
    )
    data = [fig]

    period2_fig = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return [period1_fig, period2_fig]
