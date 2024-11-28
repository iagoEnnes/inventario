import sqlite3 as lite

l_imagem = None

# Conexão com o banco de dados
conec = lite.connect('dados.db')

# Função para criar a tabela, se não existir
def criar_tabela():
    with conec:
        curs = conec.cursor()
        curs.execute("""
        CREATE TABLE IF NOT EXISTS inventario (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            item TEXT,
            quantia TEXT,
            data_guardado DATE,
            descricao TEXT,
            imagem TEXT
        )
        """)
        print("Tabela 'inventario' garantida no banco de dados.")

# Chama a função para criar a tabela
criar_tabela()

# Inserir dados
def inserir_formulario(i):
    with conec:
        curs = conec.cursor()
        i.insert(0, proximo_id())
        query = "INSERT INTO inventario(id, nome, item, quantia, data_guardado, descricao, imagem) VALUES(?,?,?,?,?,?,?)"
        curs.execute(query, i)

# Atualizar dados
def atualizar_formulario(i):
    with conec:
        curs = conec.cursor()
        query = "UPDATE inventario SET nome=?, item=?, quantia=?, data_guardado=?, descricao=?, imagem=? WHERE id=?"
        curs.execute(query, i)
        conec.commit()

# Deletar dados
def deletar_formulario(i):
    with conec:
        curs = conec.cursor()
        query = "DELETE FROM inventario WHERE id=?"
        curs.execute(query, i)

# Ver dados
def ver_formulario():
    ver_dados = []
    with conec:
        curs = conec.cursor()
        query = "SELECT * FROM inventario"
        curs.execute(query)

        rows = curs.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados

# Ver um item específico
def ver_item(id):
    ver_dados_individual = []
    with conec:
        curs = conec.cursor()
        query = "SELECT * FROM inventario WHERE id=?"
        curs.execute(query, id)

        rows = curs.fetchall()
        for row in rows:
            ver_dados_individual.append(row)
    return ver_dados_individual

# Gerar o próximo ID
def proximo_id():
    with conec:
        curs = conec.cursor()
        curs.execute("SELECT COALESCE(MAX(id), 0) + 1 FROM inventario")
        next_id = curs.fetchone()[0]
    return next_id

# Limpar a imagem do frame
def limpar_imagem():
    global l_imagem
    if l_imagem is not None:
        l_imagem.destroy()
        l_imagem = None
