import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from telegram import enviar_mensagem
from database import conectar_database
import time

# Carregar variáveis de ambiente
load_dotenv()
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
DATABASE = os.getenv('DATABASE')
PORT = os.getenv('PORT') 
HOST = os.getenv('HOST')

# Obter ID Telegram
def obter_id_telegram(id: int):

    try:

        conexao = conectar_database()
        cursor = conexao.cursor()
        cursor.execute("select userID_Telegram from usuarios where id = %s;", (id,))

        id_telegram = cursor.fetchone()
        print(f'Id TELEGRAM: {id_telegram[0]}')
        return id_telegram[0]

    except Exception as error:
        print(f"erro método 'obter_id_enviar_mensagem_telegram': ", error)
    finally:
        conexao.close()

if __name__ == "__main__":
    pass