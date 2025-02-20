from repository import create_tables, incluir_LLMs
from telegram import iniciar_telebot
from database import criar_database
from responder_mensagens import rpa_responder_mensagens
from api_enviar_resposta import montar_API
import threading

def montar_aplicacao():

    # Inicialização do banco de dados e suas respectivas tabelas:
    criar_database()
    create_tables()
    incluir_LLMs()
    
    # Criar threads para os outros métodos
    # O iniciar_telebot será executado na main thread para evitar o erro
    thread_api = threading.Thread(target=montar_API)
    
    # Inicializa as threads
    thread_api.start()

    # Iniciar o bot na thread principal
    iniciar_telebot()

montar_aplicacao()