#!/usr/bin/python3
import sqlite3
"""
Database Creation
"""


class dbModel():
    conn = sqlite3.connect("EmyDictionary.db")
    cur = conn.cursor()
    def __init__(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS (id INTEGER PRIMARY KEY, keyword STRING, meanings TEXT)")
        self.conn.commit()
        self.conn.close()

    def insert_into_db(self, keyword, meanings):
        self.cur.execute("INSERT INTO EmyDictionary VALUES (NULL, ?, ?)", (keyword, meanings))
        self.conn.commit()
        self.conn.close()
        
    def find(self):
        pass

    def close_db(self):
        self.conn.close()
