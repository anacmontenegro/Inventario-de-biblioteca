import sqlite3 as lite

con = lite.connect('dados.db')

with con:
    cur=con.cursor()
    cur.execute("CREATE TABLE inventario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, autor TEXT, isbn TEXT, editora TEXT, data_da_compra DATE, valor_da_compra DECIMAL, obs TEXT, imagem TEXT)")
