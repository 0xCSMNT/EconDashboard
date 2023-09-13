from dotenv import load_dotenv
from flask import Flask, render_template
from get_data import data_sources
import json
import os
from pymongo import MongoClient
import time

load_dotenv()

MONGO_URI = os.environ.get('MONGO_URI')
client = None
db = None

app = Flask(__name__)

def get_db():
    global client, db
    if client is None:
        MONGO_URI = os.environ.get('MONGO_URI')
        client = MongoClient(MONGO_URI)
        db = client['econ-dash-db']
    return db

def get_series(series_code):
    db= get_db()    
    fred_data = db.fred.find_one({})
    series = fred_data.get(series_code)        
    for item in series:
        try:
            item['y'] = float(item['y'])
        except ValueError:
            # Value can't be converted to float; setting it to None or some default value
            item['y'] = '.'
    return series


def get_series_pc_change(series_code):
    db=get_db()
    fred_data = db.fred.find_one({})    
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


@app.route('/dashboard')
def dashboard():
    gdp_change = get_series_pc_change('GDP')
    m2_change = get_series_pc_change('M2SL')
          
    data = {}       
    for source in data_sources:
        data[source['code'].lower()] = get_series(source['code'])
    return render_template('dashboard.html', gdp_change=gdp_change, m2_change=m2_change, **data)   
        

if __name__ == '__main__':    
    app.run(host='0.0.0.0', debug=False) # production
    # app.run(host='127.0.0.1', debug=True) # debugging