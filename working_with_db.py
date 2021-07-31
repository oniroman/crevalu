import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB <" + path + "> successfull")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


create_tete_table = """
CREATE TABLE IF NOT EXISTS tete (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  titre TEXT NOT NULL,
  type TEXT NOT NULL,
  classe TEXT NOT NULL,
  date TEXT,
  total INTEGER
);
"""
add_new_tete = """
INSERT INTO tete (titre, type, classe, date, total)
VALUES ('GR Le passé composé', 'GR', '5TSO', '2021-09-10', 10)
"""
connection = create_connection('fran.db')
execute_query(connection, create_tete_table)
execute_query(connection, add_new_tete)
result1 = execute_read_query(connection, "SELECT * FROM tete")
print(result1)
