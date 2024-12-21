from repository import create_tables, incluir_LLMs
from telegram import iniciar_telebot
from database import criar_database

def montar_aplicacao():

    # Inicialização do banco de dados e suas respectivas tabelas:
    criar_database()
    create_tables()
    incluir_LLMs()
    
    # inicializar TELEBOT:
    iniciar_telebot()

montar_aplicacao()