import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from entidades import User, Message
from tables import Usuario, Mensagem, Base, LLM, Configs

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

def incluir_LLMs():
    try:
        # Verificar se já existem registros na tabela LLM
        existing_count = session.query(LLM).count()
        if existing_count > 0:
            print("LLM values already exist. Skipping insertion.")
            return

        # Inserir valores iniciais
        llms = [
            LLM(id=1, llm="GroqAI"),
            LLM(id=2, llm="ChatGPT"),
            LLM(id=3, llm="Gemini"),
        ]
        session.add_all(llms)
        session.commit()

        session.add(Configs(id=1, campo='llm', valor='GroqAI'))
        session.commit()

        print("...Incluindo valores de migration na tablema LLM \n...GroqAI setada como IA")
    except Exception as e:
        session.rollback()
        print(f"Error inserting LLM values: {e}")

def select_config():
    try:
        # buscar IA configurada pelo usuário para analisas as mensagens:
        with engine.connect() as connection:
            # objetos em mapping
            result = connection.execute(text("select valor from configs where campo ='llm';")).mappings()
            ia = [row['valor'] for row in result]
        return ia[0]
    except Exception as e:
        print(f"Error fetching configurations: {e}")
        return []    

def salvar_nova_mensagem(usuario: User, mensagem: Message, llm_selected: str):
    try:
        # Verificar se o usuário já existe no banco de dados
        usuario_bd = session.query(Usuario).filter_by(userID_Telegram=usuario.userID_Telegram).first()
        id_llm = session.query(LLM.id).filter_by(llm=llm_selected).scalar()

        if not usuario_bd:
            # Se o usuário não existir, cria e insere no banco
            usuario_bd = Usuario(
                nome=usuario.nome, 
                sobrenome=usuario.sobrenome, 
                userID_Telegram=usuario.userID_Telegram
            )
            session.add(usuario_bd)
            session.commit()

        # Criar nova mensagem associada ao usuário
        nova_mensagem = Mensagem(
            usuario_id=usuario_bd.id,
            texto_msg=mensagem.texto_msg,
            timestamp=mensagem.timestamp,
            tipo_mensagem=mensagem.tipo_mensagem,
            respondido=mensagem.respondido,
            resposta=mensagem.resposta,

            # se IA não analisar corretamente, valor será NONE/NULL.
            llm_id=id_llm,
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
