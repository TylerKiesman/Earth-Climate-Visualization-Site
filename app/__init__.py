from flask import Flask
from app.generateFigs import *
app = Flask(__name__)

global_data = generate_global_data()
yearly_fig = global_data[0]
prediction_val = global_data[1]

period_figs = generate_choropleth_maps()
period1_fig = period_figs[0]
period2_fig = period_figs[1]

from app import routes