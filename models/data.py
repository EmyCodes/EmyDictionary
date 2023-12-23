#!/usr/bin/python3

import json
import os


def load_data():
    file_path = os.path.join(os.path.dirname(__file__), "data.json")
    with open(file_path, mode="r", encoding="utf-8") as f:
        load_data = json.load(f)
        return load_data