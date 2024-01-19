#!/usr/bin/python3

import json
import os

file_path = os.path.join(os.path.dirname(__file__), "data.json")
with open(file_path, mode="r", encoding="utf-8") as f:
    data = json.load(f)
