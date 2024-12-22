from repository import create_tables, incluir_LLMs
from telegram import iniciar_telebot
from database import criar_database
from responder_mensagens import rpa_responder_mensagens
import threading

def montar_aplicacao():

    # Inicialização do banco de dados e suas respectivas tabelas:
    criar_database()
    create_tables()
    incluir_LLMs()
    
    # Criação de threads para os métodos iniciar_telebot e rpa_responder_mensagens
    thread_telebot = threading.Thread(target=iniciar_telebot)
    thread_rpa = threading.Thread(target=rpa_responder_mensagens)

    # Inicializa as threads
    thread_telebot.start()
    thread_rpa.start()

montar_aplicacao()