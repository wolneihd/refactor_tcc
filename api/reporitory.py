import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from entidades import User, Message

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

def select_all_mensagens():
    with engine.connect() as connection:
        # objetos em mapping
        usuarios = connection.execute(text("SELECT * FROM usuarios")).mappings()
        usuarios = [row for row in usuarios]  # Cada linha já é um dicionário
        mensagens = connection.execute(text("SELECT * FROM mensagens")).mappings()
        mensagens = [row for row in mensagens]  # Cada linha já é um dicionário
        llms = connection.execute(text("SELECT * FROM llm")).mappings()
        llms = [row for row in llms]  # Cada linha já é um dicionário

        # objetos em dicionários:
        users = User.to_dict(usuarios)

        # Instanciando a classe Message para chamar o método to_dict
        message_instance = Message()
        messages = message_instance.to_dict(mensagens=mensagens, llms=llms)

        # inserindo as mensagens por usuários:
        for usuario in users:
            for mensagem in messages:
                if usuario['id'] == mensagem['usuario_id']:
                    usuario['mensagens'].append(mensagem)
        return users

if __name__ == "__main__":
    print(select_all_mensagens())