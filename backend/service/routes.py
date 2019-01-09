from flask import jsonify
from flask import request
import urllib2

from service.app import app
from service.config import Config
import json
import string
import numpy as np

global data
storedData = {}
user_ip = None

global path = '' 

# @app.before_first_request
def setup():
    pass


@app.route('/api/datareq', methods=['GET'])
def datareq():
    coin = request.headers['Coin']
    market_buy = request.headers['Market_Buy']
    market_sell = request.headers['Market_Sell']
    number_of_pulls = 100
    market_data = loadJson()
    
    times = []
    arb_values = []
    selected_data = market_data[-number_of_pulls::1]
    for run in selected_data:
        times.append(run[time])
        arb_values.append(run['margins'][coin][market_buy][market_sell])
    output_dict = {'times' : times, 'values': arb_values }
    
    return json.dumps(output_dict)

@app.route('/', methods=['GET'])
def home2():
    return ('Welcome to a link to the Blackfynn API. Documentation coming soon but for now'
            + 'check out https://github.com/Tehsurfer/Physiome-Blackfynn-API')


def loadJson():
    filename = ''
    global path
    with open(path + filename, 'r') as f:
        return json.load(f) 
    
