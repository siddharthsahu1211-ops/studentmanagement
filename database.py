import sqlite3
from datatime import datartime 

DB_FILE = 'student.db'


def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory= sqlite3.Row 
    return conn