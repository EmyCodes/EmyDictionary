#!/usr/bin/python3
import json
import sqlite3

from data import data
"""
Database Creation
"""
# for k, v in data.items():
#     print()
#     print(f"{k}:  {v}")

class dbModel():
    conn = sqlite3.connect("EmyDictionary.db")
    cur = conn.cursor()

    def __init__(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS EmyDictionary (id INTEGER PRIMARY KEY, keyword STRING, meanings TEXT)")
        self.conn.commit()

    def insert_into_db(self):
        for key, value in data.items():
            value_str = json.dumps(value)
            self.cur.execute("INSERT INTO EmyDictionary VALUES (NULL, ?, ?)", (key, value_str))
            self.conn.commit()
            
    def close_db(self):
        self.conn.close()
        # if self.conn.close:
        #     print("Closed")

db = dbModel()
# db.insert_into_db()
# db.find()
# db.close_db()