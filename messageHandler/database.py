import mysql.connector;
from dotenv import load_dotenv
import os

# Carrega as variáveis do arquivo .env
load_dotenv()

# Acesse as variáveis usando os.environ
db_user = os.getenv('USER')
db_password = os.getenv('PASSWORD')
db_port = os.getenv('PORT')
db_host = os.getenv('HOST')
db_name = os.getenv('DATABASE')

# configurações do BD como um dicionário
config = {
    'host': db_host,
    'port': db_port,
    'user': db_user,
    'password': db_password,
}

def conectar():
    conexao = mysql.connector.connect(
        host=db_host,
        port=db_port,
        user=db_user,
        password=db_password,
    )
    return conexao

def conectar_database():
    conexao = mysql.connector.connect(
        host=db_host,
        port=db_port,
        user=db_user,
        password=db_password,
        database=db_name
    )
    return conexao

def criar_database():
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name};")
        print('Database criado/já existente.')
    except Exception as error:
        print(f'Erro ao criar database {db_name}: ', error)
    finally:
        conexao.commit()
        conexao.close()

if __name__ == "__main__":
    criar_database()
