#!/usr/bin/python3
import json
import sqlite3


"""
Database Creation
"""



class dbModel():
    """
    This class handles all the database operations.
    Attributes:\n
        conn (sqlite3.Connection): The connection object for the database.\n
        cur (sqlite3.Cursor): The cursor object for the database.
    """
    conn = sqlite3.connect("EmyDictionary.db")
    cur = conn.cursor()

    def __init__(self):
        """
        Creates the database and the table if they don't exist.
        Returns:\n
            None
        """
        self.conn = sqlite3.connect("EmyDictionary.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS EmyDictionary (id INTEGER PRIMARY KEY, keyword STRING, meanings TEXT)")
        self.conn.commit()

    def insert_into_db(self):
        """
        Inserts the data into the database.
        Returns:\n
            None
        """
        for key, value in data.items():
            value_str = json.dumps(value)
            self.cur.execute("INSERT INTO EmyDictionary VALUES (NULL, ?, ?)", (key, value_str))
            self.conn.commit()

    def get_meaning(self, keyword=""):
        """
        gets the meaning of the word from the database.
        Parameters:\n
            keyword (str): The word to be searched for in the database.
        Returns:\n
            list: A list of meanings if the word is found,
                  an empty list if the word doesn't exist.
        """
        self.cur.execute("SELECT keyword, meanings FROM EmyDictionary WHERE keyword=?", (keyword,))
        self.rows = self.cur.fetchall()
        for row in self.rows:
            print(row)
        return self.rows
            
    def close_db(self):
        """
        closes the database connection.
        """
        self.conn.close()
        # if self.conn.close:
        #     print("Closed")

db = dbModel()
# db.insert_into_db()
db.get_meaning("rain")
db.close_db()
