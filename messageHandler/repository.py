import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from entidades import User, Message
from tables import Usuario, Mensagem, Base

# Carregar variáveis de ambiente
load_dotenv()
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
DATABASE = os.getenv('DATABASE')
PORT = os.getenv('PORT')  # Porta padrão do MySQL
HOST = os.getenv('HOST')

# URL de conexão com o MySQL
DATABASE_URL = f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
Session = sessionmaker(bind=engine)
session = Session()

def create_tables():
    try:
        print("Creating tables if they don't exist...")
        Base.metadata.create_all(engine)
        print("Tables successfully created or already exist.")
    except Exception as e:
        print(f"Error creating tables: {e}")

def salvar_nova_mensagem(usuario: User, mensagem: Message):
    try:
        # Verificar se o usuário já existe no banco de dados
        usuario_bd = session.query(Usuario).filter_by(userID_Telegram=usuario.userID_Telegram).first()

        if not usuario_bd:
            # Se o usuário não existir, cria e insere no banco
            usuario_bd = Usuario(nome=usuario.nome, sobrenome=usuario.sobrenome, userID_Telegram=usuario.userID_Telegram)
            session.add(usuario_bd)
            session.commit()

        # Criar nova mensagem associada ao usuário
        nova_mensagem = Mensagem(
            usuario_id=usuario_bd.id,
            texto_msg=mensagem.texto_msg,
            timestamp=mensagem.timestamp,
            tipo_mensagem=mensagem.tipo_mensagem,

            # se IA não analisar corretamente, valor será NONE/NULL.
            analise_ia=mensagem.analiseIA,
            categoria=mensagem.categoria,
            feedback=mensagem.feedback,
        )

        # Adicionar e salvar a nova mensagem
        session.add(nova_mensagem)
        session.commit()

        print("Mensagem salva com sucesso!")
    except Exception as e:
        print(f"Error inserting data: {e}")
        session.rollback()  
