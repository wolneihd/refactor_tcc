import os
import telebot
from dotenv import load_dotenv
import random
import string

from entidades import User, Message
from repository import salvar_nova_mensagem, select_config
from audio_handler import convert_audio, transcribe_audio

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
    salvar_nova_mensagem(usuario, mensagem, mensagem.llm)
    bot.send_message(message.chat.id, "mensagem recebida, estaremos analisando.")

## Handler para mensagens em audio
@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    # Baixa o arquivo de áudio
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    # Salva o arquivo OGG
    ogg_file_path = 'audio.ogg'
    with open(ogg_file_path, 'wb') as new_file:
        new_file.write(downloaded_file)

    # Converte OGG para WAV
    wav_file_path = 'audio.wav'
    convert_audio(ogg_file_path, wav_file_path)

    # Transcreve o áudio
    transcription = transcribe_audio(wav_file_path)

    # Salva informação no banco de dados
    llm = select_config()
    usuario = User(message.from_user) 
    mensagem = Message(message, llm, transcription)
    salvar_nova_mensagem(usuario, mensagem, mensagem.llm)
    bot.send_message(message.chat.id, "Mensagem de aúdio recebida, estaremos analisando.")

## Handler para mensagens tipo Imagem
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    # Obtém o arquivo da imagem
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    caracteres = string.ascii_letters + string.digits
    nome_arquivo = ''.join(random.choice(caracteres) for _ in range(15))

    # Define o caminho para salvar a imagem
    image_path = os.path.join('images', f'{nome_arquivo}.jpg')

    # Salva a imagem na pasta 'images'
    with open(image_path, 'wb') as new_file:
        new_file.write(downloaded_file)

    # save_message_DB(message)
    bot.send_message(message.chat.id, "Imagem recebida, estaremos analisando.")

def enviar_mensagem(user_id: int, resposta: str):
    try:
        bot.send_message(user_id, resposta)
        print(f"resposta enviada para o user_id {user_id}: {resposta}")
    except Exception as e:
        print(f"Erro ao enviar resposta para o user_id {user_id}: {str(e)}")

def iniciar_telebot():
    print("\nbot/aplicação inicializada...")
    bot.polling(none_stop=True)
