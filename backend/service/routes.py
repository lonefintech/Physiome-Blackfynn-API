from flask import jsonify
from flask import request
from blackfynn import Blackfynn

from service.app import app
from service.config import Config
import json

bf = None

# NOTE: connect_to_blackfynn() is a temporary workaround that can be used to login to Blackfynn without
# having to make a POST request

# @app.before_first_request
def connect_to_blackfynn():
    global bf
    bf = Blackfynn(
        api_token=Config.BLACKFYNN_API_TOKEN,
        api_secret=Config.BLACKFYNN_API_SECRET,
        env_override=False,
        host=Config.BLACKFYNN_API_HOST,
        concepts_api_host=Config.BLACKFYNN_CONCEPTS_API_HOST
    )


@app.route('/api/', methods=['GET'])
def home():
    return ('Welcome to a link to the Blackfynn API. Documentation coming soon but for now'
            + 'check out https://github.com/Tehsurfer/Physiome-Blackfynn-API')

@app.route('/api/dataset/<id>', methods=['GET'])
def dataset(id):
    dataset = bf.get_dataset(id)
    return 'Dataset: {}'.format(dataset.name)


# This route logs in with a given api token and secret and returns the available 
@app.route('/api/get_timeseries_dataset_names', methods=['POST'])
def get_timeseries_dataset_names():
    data = json.loads(request.data.decode("utf-8"))

    global bf
    bf = Blackfynn(api_token=data['tokenId'], api_secret=data['secret'])
    data_sets = bf.datasets()

    global time_series_items
    time_series_items = []
    time_series_names = []
    for data_set in data_sets:
        for item in data_set.items:
            if item.type is 'TimeSeries':
                time_series_items.append(item)
                time_series_names.append(item.name)

    return json.dumps({'names': time_series_names})

# /api/get_channel_data: Returns the data relating to the first channel of a given
#      dataset
@app.route('/api/get_channel_data', methods=['GET'])
def datasets():

    name = request.headers['Name']
    channel = request.headers['Channel']

    global bf
    global time_series_items
    data = []
    channel_array = []
    for item in time_series_items:
        print(item.name)
        if item.name == name:
            data = item.get_data(length='2s')
    for key in data:
        channel_array = data[key]
        break
    return json.dumps({'data': str(channel_array.tolist())})

# /api/get_channels: Returns channel names for a given dataset
@app.route('/api/get_channels', methods=['GET'])
def channels():
    name = request.headers['Name']
    global bf
    global time_series_items
    data = []
    channel_names = []
    for item in time_series_items:
        print(item.name)
        if item.name == name:
            data = item.get_data(length='1s')
    for key in data:
        channel_names.append(key)
    return json.dumps({'data': channel_names}) 

# /api/get_channel: Returns data for a single channel
@app.route('/api/get_channel', methods=['GET'])
name = request.headers['Name']
    requested_channel = request.headers['Channel']
    requested_channel = requested_channel.decode("utf-8")
    print('request is:' + requested_channel)
    global bf
    global time_series_items
    data = []
    channel_names = []
    for item in time_series_items:
        if item.name == name:
            for channel in item.channels:
                if channel.name is requested_channel:
                    data = channel.get_data(length='2s')

    return json.dumps({'data': str(data[requested_channel].tolist())})

