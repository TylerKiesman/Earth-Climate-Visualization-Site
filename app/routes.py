from flask import render_template
from app import app
from app import lineJSON, prediction_val

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', plot=lineJSON, pred=prediction_val)