#!/usr/bin/python3
import json
import sqlite3
import os

"""
Database Creation
"""

# Load the data from the json file
file_path = os.path.join(os.path.dirname(__file__), "data.json")
with open(file_path, mode="r", encoding="utf-8") as f:
    data = json.load(f)


class dbModel():
    """
    This class handles all the database operations.
    Attributes:\n
        conn (sqlite3.Connection): The connection object for the database.\n
        cur (sqlite3.Cursor): The cursor object for the database.
    """
    conn = sqlite3.connect("EmyDictionary.db")
    cur = conn.cursor()
    contain = ""

    def __init__(self):
        """
        Creates the database and the table if they don't exist.
        """
        self.conn = sqlite3.connect("EmyDictionary.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS EmyDictionary (id INTEGER PRIMARY KEY, keyword STRING, meanings TEXT)")
        self.conn.commit()

    def insert_into_db(self):
        """
        Inserts the data into the database.
        """
        for key, value in data.items():
            value_str = json.dumps(value)
            self.cur.execute("INSERT INTO EmyDictionary VALUES (NULL, ?, ?)", (key, value_str))
            self.conn.commit()

    def get_meaning(self, keyword=""):
        """
        Gets the meaning of the word from the database.
        Parameters:\n
            keyword (str): The word to be searched for in the database.
        Returns:\n
            list: A list of meanings if the word is found,
                  an empty list if the word doesn't exist.
        """
        self.cur.execute("SELECT keyword, meanings FROM EmyDictionary WHERE keyword=?", (keyword,))
        self.rows = self.cur.fetchall()
        return self.rows

    def get_all(self, contains=""):
        """
        Returns all 'contain' match-keyword in the database
        """
        if contains is None:
            return []
        n = len(contains)
        if n < 4:
            self.cur.execute("SELECT keyword FROM EmyDictionary WHERE keyword LIKE ?", (f"{contains[0:2]}%",))
        else:
            self.cur.execute("SELECT keyword FROM EmyDictionary WHERE keyword LIKE ?", (f"{contains[0:3]}%",))
        self.rows = self.cur.fetchall()
        return self.rows
            
    def close_db(self):
        """
        closes the database connection.
        """
        self.conn.close()
