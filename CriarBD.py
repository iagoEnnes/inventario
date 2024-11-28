import sqlite3 as lite
import os

# Definir o nome do banco de dados
database_name = 'dados.db'

# Função para criar o banco de dados e a tabela, se não existir
def setup_database():
    # Verifica se o arquivo do banco de dados já existe
    if not os.path.exists(database_name):
        print(f"Banco de dados '{database_name}' não encontrado. Criando...")
        conec = lite.connect(database_name)
        with conec:
            curs = conec.cursor()
            # Cria a tabela 'inventario' se ela não existir
            curs.execute("""
            CREATE TABLE inventario (
                id INTEGER PRIMARY KEY,
                nome TEXT,
                item TEXT,
                quantia TEXT,
                data_guardado DATE,
                descricao TEXT,
                imagem TEXT
            )
            """)
            print("Tabela 'inventario' criada com sucesso!")
    else:
        # Verifica se a tabela já existe no banco
        conec = lite.connect(database_name)
        with conec:
            curs = conec.cursor()
            curs.execute("""
            SELECT name FROM sqlite_master WHERE type='table' AND name='inventario';
            """)
            result = curs.fetchone()
            if result:
                print("Tabela 'inventario' já existe. Banco de dados pronto para uso.")
            else:
                print("Tabela 'inventario' não encontrada. Criando...")
                curs.execute("""
                CREATE TABLE inventario (
                    id INTEGER PRIMARY KEY,
                    nome TEXT,
                    item TEXT,
                    quantia TEXT,
                    data_guardado DATE,
                    descricao TEXT,
                    imagem TEXT
                )
                """)
                print("Tabela 'inventario' criada com sucesso!")

# Chamar a função para configurar o banco de dados
setup_database()
