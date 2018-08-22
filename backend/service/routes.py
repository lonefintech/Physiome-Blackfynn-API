from flask import jsonify
from blackfynn import Blackfynn

from service.app import app
from service.config import Config

bf = None

# NOTE: connect_to_blackfynn() is a temporary workaround that can be used to login to Blackfynn
#       on my account

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
    return 'Welcome to a link to the Blackfynn API. Documentation coming soon but for now check out https://github.com/Tehsurfer/flask-vue'


@app.route('/api/dataset/<id>', methods=['GET'])
def dataset(id):
    dataset = bf.get_dataset(id)2
    return 'Dataset: {}'.format(dataset.name)


# This route logs in with a given api token and secret and returns the available 
@app.route('/api/get_timeseries_dataset_names', methods=['POST'])
def get_timeseries_dataset_names():
    data = json.loads(request.data.decode("utf-8"))

    global bf
    bf = blackfynn.Blackfynn(api_token=data['tokenId'], api_secret=data['secret'])
    data_sets = bf.datasets()

    global time_series_items
    time_series_items = []
    time_series_names = []
    for data_set in data_sets:
        for item in data_set.items:
            if item.type is 'TimeSeries':
                time_series_items.append(item)
                time_series_names.append(item.name)

    return json.dumps({'time_series_names': time_series_names})

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
            data = item.get_data(length='1s')
    for key in data:
        channel_array = data[key]
        break
    return json.dumps({'data': str(channel_array.tolist())})
