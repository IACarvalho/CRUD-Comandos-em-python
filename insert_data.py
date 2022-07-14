import sqlite3

from colorama import Cursor

connection = sqlite3.connect('crud.db')
cursor = connection.cursor()

query_sql = """
  INSERT INTO users(name, surname, cpf)
  VALUES('Fulano', 'de Tal', '00000000000')
"""

cursor.execute(query_sql)
connection.commit()
connection.close()