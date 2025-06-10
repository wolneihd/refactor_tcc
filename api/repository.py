import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from entidades import User, Message
from tables import Base, Totem, UsuariosSistema
from database import conectar_database

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

def create_tables():
    try:
        print("Creating tables if they don't exist...")
        Base.metadata.create_all(engine)
        print("Tables successfully created or already exist.")
    except Exception as e:
        print(f"Error creating tables: {e}")

def select_all_mensagens():
    with engine.connect() as connection:
        # objetos em mapping

        usuarios = connection.execute(text("SELECT * FROM usuarios;")).mappings()
        usuarios = [row for row in usuarios]  # Cada linha já é um dicionário

        mensagens = connection.execute(text("SELECT * FROM mensagens;")).mappings()
        mensagens = [row for row in mensagens]  # Cada linha já é um dicionário

        # objetos em dicionários:
        users = User.to_dict(usuarios)

        # Instanciando a classe Message para chamar o método to_dict
        messages = Message.to_dict(mensagens=mensagens)

        # inserindo as mensagens por usuários:
        for usuario in users:
            for mensagem in messages:
                if usuario.get('id') == mensagem.get('usuario_id'):
                    usuario['mensagens'].append(mensagem)
        return users

# Função corrigida para inserir um registro
def insert_feedback_totem(status_totem: str):
    try:
        novo_totem = Totem(status=status_totem) 
        session.add(novo_totem)
        session.commit()
        session.refresh(novo_totem)  # Atualiza o objeto com os dados do BD
        return f'Mensagem salva com sucesso! ID: {novo_totem.id}'
    except Exception as error:
        session.rollback()  # Reverte alterações em caso de erro
        return f'Erro ao salvar no BD: {error}'
    finally:
        session.close()  # Fecha a sessão para evitar conexões abertas

def atualizar_resposta_bd(ids: list, resposta: str):
    try:
        conexao = conectar_database()
        cursor = conexao.cursor()

        for id in ids:
            cursor.execute("UPDATE mensagens SET resposta = %s WHERE id = %s", (resposta, id))
            cursor.execute("UPDATE mensagens SET respondido = true WHERE id = %s", (id,))
            conexao.commit()
            print(f'id {id} atualizado com sucesso!')

    except Exception as error:
        print('Erro ao atualizar BD: ', error)
    finally:
        session.close()  # Fecha a sessão para evitar conexões abertas

def select_filter(
        nome: str = None,        
        status: int = None,
        llm_selecionada: int = None,
        analise_ia: str = None,
        tipo: str = None,
        timestamp_data_de: int = None,
        timestamp_data_ate: int = None,
        categoria: str = None,
        ):
    try:
        conexao = conectar_database()
        cursor = conexao.cursor()

        # Busca dos Usuários:
        if (nome):
            cursor.execute("""SELECT * FROM usuarios WHERE  ((nome IS NULL OR nome LIKE  %s) OR (sobrenome IS NULL OR sobrenome LIKE %s))""", (nome, nome))
        else:
            cursor.execute("SELECT * FROM usuarios;")

        pessoas = []       
        registros = cursor.fetchall()
        for registro in registros:
            pessoa = {}
            pessoa['id'] = registro[0]
            pessoa['nome'] = registro[1]
            pessoa['sobrenome'] = registro[2]
            pessoa['userID_Telegram'] = registro[3]
            pessoa['mensagens'] = []
            pessoas.append(pessoa)

        # Busca das Mensagens:
        query = """
            SELECT * FROM mensagens
            WHERE 
                (
                    (%s IS NULL OR respondido LIKE %s)
                    AND
                    (%s IS NULL OR llm_id LIKE %s)
                    AND
                    (%s IS NULL OR analise_ia LIKE %s)
                    AND
                    (%s IS NULL OR categoria LIKE %s)
                    AND
                    (%s IS NULL OR tipo_mensagem LIKE %s)
                    AND
                    (%s IS NULL OR timestamp > %s)
                    AND
                    (%s IS NULL OR timestamp < %s)
                );
        """

        params = (status, status, llm_selecionada, llm_selecionada, analise_ia, analise_ia, categoria, categoria,
                  tipo, tipo, timestamp_data_de, timestamp_data_de, timestamp_data_ate, timestamp_data_ate)
        cursor.execute(query, params)
        
        mensagens = []
        registros = cursor.fetchall()
        for registro in registros:
            mensagem = {}
            mensagem['id'] = registro[0]
            mensagem['usuario_id'] = registro[1]
            mensagem['texto_msg'] = registro[2]
            mensagem['timestamp'] = registro[3]
            mensagem['tipo_mensagem'] = registro[4]
            mensagem['respondido'] = registro[5]
            mensagem['nome_imagem'] = registro[6]
            mensagem['llm_id'] = registro[7]
            mensagem['analise_ia'] = registro[8]
            mensagem['categoria'] = registro[9]
            mensagem['feedback'] = registro[10]
            mensagem['resposta'] = registro[11]
            mensagens.append(mensagem)

        for mensagem in mensagens:
            for usuario in pessoas:
                if (usuario['id'] == mensagem['usuario_id']):
                    usuario['mensagens'].append(mensagem)

        return pessoas

    except Exception as error:
        print(f'Erro ao buscar filtrado: {error}', flush=True)
    finally:
        conexao.close()

def buscar_mensagens_totem():

    data = []

    for opcao in ['positivo', 'neutro', 'negativo']: 
        try:
            conexao = conectar_database()
            cursor = conexao.cursor()
            cursor.execute('SELECT COUNT(*) FROM totem where status=%s;', (opcao,))        
            resposta = cursor.fetchone()
            # print(resposta, flush=True)

            data.append({
                "name": opcao,
                "value": resposta[0]
            })
        except Exception as error:
            print(f'Erro ao buscar filtrado: {error}', flush=True)
            data.append({
                "name": opcao,
                "value": None
            })
        finally:
            conexao.close()

    return data

def buscar_todas_llms():

    data = []

    try:
        conexao = conectar_database()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM llm;')        
        resposta = cursor.fetchall()
        for valor in resposta: 
            data.append({
                "id": valor[0],
                "ia": valor[1]
            })
    except Exception as error:
        print(f'Erro ao buscar filtrado: {error}', flush=True)
    finally:
        conexao.close()

    return data

def atualizar_ia(llm: str):
    try:
        conexao = conectar_database()
        cursor = conexao.cursor()

        cursor.execute('update configs set valor = %s where campo="llm";', (llm, ))
        conexao.commit()

        print(f'LLM atualizada com sucesso no BD para {llm}', flush=True)

    except Exception as error:
        print('Erro ao atualizar BD: ', error)
    finally:
        session.close()  # Fecha a sessão para evitar conexões abertas

# Função corrigida para inserir um registro
def salvar_novo_usuario(nome: str, email: str):
    try:
        novo_usuario = UsuariosSistema(
            nome = nome,
            email = email,
            status = True
        ) 
        session.add(novo_usuario)
        session.commit()
        session.refresh(novo_usuario)  # Atualiza o objeto com os dados do BD
        return f'Mensagem salva com sucesso! ID: {novo_usuario.id}'
    except Exception as error:
        session.rollback()  # Reverte alterações em caso de erro
        return f'Erro ao salvar no BD: {error}'
    finally:
        session.close()  # Fecha a sessão para evitar conexões abertas

def buscar_todos_usuarios():

    data = []

    try:
        conexao = conectar_database()
        cursor = conexao.cursor()
        cursor.execute('select * from usuarios_sistema;')        
        resposta = cursor.fetchall()
        for valor in resposta: 
            data.append({
                "id": valor[0],
                "nome": valor[1],
                "email": valor[2],
                "status": valor[3],
            })
    except Exception as error:
        print(f'Erro ao buscar filtrado: {error}', flush=True)
    finally:
        conexao.close()

    return data

if __name__ == "__main__":
    print(select_all_mensagens())