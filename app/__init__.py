from flask import Flask
import os
from app.generatePoints import *
import plotly.express as px
import plotly
import pandas as pd
import json

curDir = os.path.dirname(__file__)
global_temp_path = os.path.abspath(os.path.join(curDir, "..", "data", "GlobalTemperatures.csv"))
l_and_o_yearly_data = land_and_ocean_yearly(global_temp_path)
year_to_temps = l_and_o_yearly_data[0]
df = pd.DataFrame(columns=["Year", "Average Global Temperature"])
for year in year_to_temps:
    df2 = pd.DataFrame([[year, year_to_temps.get(year)]], columns=["Year", "Average Global Temperature"])
    df = df.append(df2)
fig = px.line(df, x="Year", y="Average Global Temperature", title='Test')
data = [fig]

lineJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

app = Flask(__name__)

from app import routes