import sqlite3

connection = sqlite3.connect('crud.db') # Cria o banco de dados caso não exista e estabelece conexão com ele
cursor = connection.cursor() # Cria um cursor para executar os comandos SQL (query sql)

# Query SQL
query_sql = """
CREATE TABLE users  (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  surname TEXT,
  cpf TEXT NOT NULL UNIQUE
)
"""

cursor.execute(query_sql) # Executa a query
connection.commit() # FInaliza a execução
connection.close() # Fecha a conexão com o banco