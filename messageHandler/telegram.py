import io
import os
import pprint
import telebot
from dotenv import load_dotenv
import random
import string

from entidades import User, Message
from repository import salvar_nova_mensagem, select_config
from audio_handler import convert_audio, transcribe_audio, convert_audio_memoria, transcribe_audio_memoria
from salvar_minio import salvar_imagem_bucket, salvar_audio_bucket

# Carregar variáveis de ambiente
load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TELEGRAM_TOKEN)

## Resposta ao iniciar o BOT
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Olá, você está no IA-Feedback-Analyser!")

## Handler para mensagens em texto
@bot.message_handler(content_types=['text'])
def handle_text(message):
    llm = select_config()
    usuario = User(message.from_user) 
    mensagem = Message(message, llm)
    salvar_nova_mensagem(
        usuario=usuario, 
        mensagem=mensagem, 
        llm_selected=mensagem.llm,
        tipo_mensagem="texto"
        )
    bot.send_message(message.chat.id, "mensagem recebida, estaremos analisando.")

## Handler para mensagens tipo Imagem
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    # Obtém o arquivo da imagem
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    nome_arquivo, resposta = salvar_imagem_bucket(
        downloaded_file=downloaded_file
        )

    try:
        usuario = User(message.from_user) 
        mensagem = Message(message, n_imagem=nome_arquivo)
        salvar_nova_mensagem(
            usuario=usuario,   
            mensagem=mensagem,
            tipo_mensagem="imagem",
            )
    except Exception as e:
        print(e)
    
    bot.send_message(message.chat.id, resposta)

def enviar_mensagem(user_id: int, resposta: str):
    try:
        bot.send_message(user_id, resposta)
        print(f"resposta enviada para o user_id {user_id}: {resposta}")
    except Exception as e:
        print(f"Erro ao enviar resposta para o user_id {user_id}: {str(e)}")      

## Handler para mensagens em audio
@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    # Baixa o arquivo de áudio
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    # atualizado para salvar audio em memória para economizar armazenamento.
    ogg_file = io.BytesIO(downloaded_file)
    wav_file = convert_audio_memoria(ogg_file)
    transcription = transcribe_audio_memoria(wav_file)

    # salvando arquivo no MinIO:
    salvar_audio_bucket(downloaded_file)

    # Salva informação no banco de dados
    llm = select_config()
    usuario = User(message.from_user) 
    mensagem = Message(
        data=message,
        transcription=transcription,
        n_audio="teste.wav",
        llm=llm
    )
    salvar_nova_mensagem(
        usuario=usuario,
        mensagem=mensagem,
        tipo_mensagem="audio",
        llm_selected=llm
    )
    bot.send_message(message.chat.id, "Mensagem de aúdio recebida, estaremos analisando.")

def iniciar_telebot():
    print("\nbot/aplicação inicializada...")
    bot.polling(none_stop=True)

if __name__ == "__main__":
    iniciar_telebot()