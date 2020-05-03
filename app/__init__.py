from flask import Flask
import os
from app.generatePoints import *

curDir = os.path.dirname(__file__)
global_temp_path = os.path.abspath(os.path.join(curDir, "..", "data", "GlobalTemperatures.csv"))
global_yearly_points = generate_global_yearly(global_temp_path)

app = Flask(__name__)

from app import routes