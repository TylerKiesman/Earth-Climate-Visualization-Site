from flask import Flask
import os
from app.generatePoints import *
import plotly.express as px
import plotly
import pandas as pd
import json
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

curDir = os.path.dirname(__file__)
global_temp_path = os.path.abspath(os.path.join(curDir, "..", "data", "GlobalTemperatures.csv"))
l_and_o_yearly_data = land_and_ocean_yearly(global_temp_path)
year_to_temps = l_and_o_yearly_data[0]
year_to_error = l_and_o_yearly_data[1]
df = pd.DataFrame(columns=["Year", "Average Global Temperature", "Error"])
for year in year_to_temps:
    df2 = pd.DataFrame([[year, year_to_temps.get(year), year_to_error.get(year)]], columns=["Year", "Average Global Temperature", "Error"])
    df = df.append(df2)
fig = px.line(df, x="Year", y="Average Global Temperature", title='Test', error_y="Error")

x = df.iloc[:, 0:1].values
y = df.iloc[:, 1].values
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(x)
poly.fit(X_poly, y)
lin = LinearRegression()
lin.fit(X_poly, y)
print(lin.predict(poly.fit_transform([[2050]])))

line_obj = fig.data[0]
line_obj.line.color = "#FF0800"
line_obj.mode = "lines+markers"
line_obj.marker = {
            "color":'#4C516D'}
line_obj.error_y.color = "black"
line_obj.error_y.thickness = .7
line_obj.error_y.width = 0
fig.update_layout(
    title="Global Average Yearly Temperature 1850 - 2015",
    yaxis_title="Global Temperature (" + u"\u2103" + ")"
)
data = [fig]

lineJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

app = Flask(__name__)

from app import routes