# Physiome-Blackfynn-API
This api is created to link the [webGL heart model](https://github.com/Tehsurfer/MPB) to the [Blackfynn Python API](https://github.com/Blackfynn/blackfynn-python)

## Backend

### Prerequisites
- pip
- virtualenv
- python 2.7

### Running the Flask App
- Create a virtual environment and activate it
- Either Open `Config.py` and update the environment variables below
  - BLACKFYNN_API_TOKEN = ""
  - BLACKFYNN_API_SECRET = ""
  or enter them later using the supplied 'index.html' front end
- Run `pip install -r requirements.txt`
- Run `python server.py` to start the flask app

## Frontend

### Prerequisites
- Node >= v8.0.0

### Check if it's running 
- Open `localhost:80` in your browser

### Use the front end tester
- Open index.html
- enter you API keys and check it fetches the repository names


