from flask import render_template, request
from app import app
from app import yearly_fig, prediction_val, period1_fig, period2_fig, year1, year2, years_after

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', plot=yearly_fig,
                           pred=prediction_val, period=period1_fig, year1=year1, year2=year2,
                           ped1=year1 + years_after, ped2=year2 + years_after)

@app.route('/updatePeriod')
def update_period():
    number = request.args.get('number')
    number = int(number)
    if number == 1:
        return period1_fig
    elif number == 2:
        return period2_fig
