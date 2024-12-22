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
        mensagens = connection.execute(text("""
            SELECT 
                mensagens.id,
                mensagens.usuario_id,
                mensagens.texto_msg,
                mensagens.timestamp,
                mensagens.tipo_mensagem,
                llm.llm,
                mensagens.analise_ia,
                mensagens.categoria,
                mensagens.feedback
                FROM mensagens
                INNER JOIN llm ON llm.id = mensagens.llm_id;
        """)).mappings()
        mensagens = [row for row in mensagens]  # Cada linha já é um dicionário

        # objetos em dicionários:
        users = User.to_dict(usuarios)

        # Instanciando a classe Message para chamar o método to_dict
        messages = Message.to_dict(mensagens=mensagens)

        # inserindo as mensagens por usuários:
        for usuario in users:
            for mensagem in messages:
                if usuario['id'] == mensagem['usuario_id']:
                    usuario['mensagens'].append(mensagem)
        return users

if __name__ == "__main__":
    print(select_all_mensagens())