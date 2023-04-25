import sqlite3 as lite

con = lite.connect('dados.db')

# ------- ADICIONAR LIVRO -------
def inserir_livro(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO inventario(nome, autor, isbn, editora, data_da_compra, valor_da_compra, obs, imagem) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query,i)

# ------- ATUALIZAR LIVRO -------
def atualizar_dados(i):
    with con:
        cur = con.cursor()
        query = "UPDATE inventario SET nome=?, autor=?, isbn=?, editora=?, data_da_compra=?, valor_da_compra=?, obs=?, imagem=? WHERE id=?"
        cur.execute(query,i)

# ------- DELETAR LIVRO -------
def deletar_dados(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM inventario WHERE id=?"
        cur.execute(query,i)

#i = [3]
#deletar_dados(i)

# ------- VER LIVROS -------
def ver_livros():
    ver_dados = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventario"
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados

#print(ver_livros())

# ------- VER LIVRO INDIVIDUAL -------
def ver_item(id):
    #id = [?] 
    ver_dado_individual = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventario WHERE id=?"
        cur.execute(query,id)
        rows = cur.fetchall()
        for row in rows:
            ver_dado_individual.append(row)
    return ver_dado_individual

#print(ver_item(id))
