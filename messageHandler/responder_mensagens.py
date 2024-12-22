import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from telegram import enviar_mensagem

import time

# Carregar variáveis de ambiente
load_dotenv()
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
DATABASE = os.getenv('DATABASE')
PORT = os.getenv('PORT') 
HOST = os.getenv('HOST')

# URL de conexão com o MySQL
DATABASE_URL = f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
Session = sessionmaker(bind=engine)
session = Session()

def rpa_responder_mensagens():
    print('inicializado monitoramento de mensagens pendentes de envio.\n')
    while True:
        time.sleep(10)
        print('Conferindo se há mensagens pendentes de respostas...')
        with engine.connect() as connection:
            # objetos em mapping
            mensagens = connection.execute(text("""
            select 
	            mensagens.id, 
                mensagens.respondido, 
                mensagens.resposta,
                usuarios.userID_Telegram
                from mensagens 
                INNER JOIN usuarios ON usuarios.id = mensagens.usuario_id
                where resposta is not NULL and respondido = 0;
            """)).mappings()
            mensagens = [row for row in mensagens]  # Cada linha já é um dicionário
            if len(mensagens) > 0:
                for mensagem in mensagens:
                    enviar_mensagem(mensagem['userID_Telegram'], mensagem['resposta'])
                    connection.execute(text(f"UPDATE mensagens set respondido = TRUE where id = {mensagem['id']};"))
                    connection.commit()
                    print(f'Mensagem id: {mensagem['id']} - atualizada para respondido.')
            else:
                print(f'Sem mensagens pendentes de atualização.')

if __name__ == "__main__":
    rpa_responder_mensagens()