import json

def load_data():
    with open("data.json", mode="r", encoding="utf-8") as f:
        load_data = json.load(f)
        return load_data