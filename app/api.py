import json

def get_api_data():
    with open("data/api_data.json") as f:
        return json.load(f)