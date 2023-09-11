from dotenv import load_dotenv
from flask import Flask, render_template
from get_data import data_sources
import json
import os
import time    

app = Flask(__name__)

def get_series(series_code):
    with open('fred_data.json', 'r') as f:
        fred_data = json.load(f)
        series = fred_data.get(series_code)
        for item in series:
            try:
                item['y'] = float(item['y'])
            except ValueError:
                # Value can't be converted to float; setting it to None or some default value
                item['y'] = '.'
    return series



def get_series_pc_change(series_code):
    with open('fred_data.json', 'r') as f:
        fred_data = json.load(f)
        data = fred_data.get(series_code)
    
    new_data = []
    for i in range(len(data) - 1):
        current_val = float(data[i]['y'])
        next_val = float(data[i + 1]['y'])
        percentage_change = ((current_val - next_val) / next_val) * 100
        new_data.append({'x': data[i]['x'], 'y': round(percentage_change, 2)})
    return new_data



@app.route('/')
def index():
    name = "Cormac"
    return render_template('index.html',name=name)


@app.route('/gdp_test')
def gdp_test():
    gdp = get_series("GDP")
    return render_template('gdp_test.html', gdp=gdp, )


@app.route('/grid_test')
def grid_test():    
    return render_template('grid_test.html' )


@app.route('/chartjs_test')
def chartjs_test():
    data = {}
    for source in data_sources:
        data[source['code'].lower()] = get_series(source['code'])
    return render_template('chartjs_test.html', **data)


@app.route('/dashboard')
def dashboard():
    gdp_change = get_series_pc_change('GDP')
    m2_change = get_series_pc_change('M2SL')
          
    data = {}       
    for source in data_sources:
        data[source['code'].lower()] = get_series(source['code'])
    return render_template('dashboard.html', gdp_change=gdp_change, m2_change=m2_change, **data)
    

        

if __name__ == '__main__':
    template_files = [os.path.join('templates', f) for f in os.listdir('templates') if f.endswith('.html')]
    app.run(debug=True, extra_files=template_files)

