from flask import render_template
from app import app
from app import yearly_fig, prediction_val, period1_fig, period2_fig

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', plot=yearly_fig, pred=prediction_val, period1=period1_fig, period2=period2_fig)
