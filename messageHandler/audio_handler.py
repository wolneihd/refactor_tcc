import speech_recognition as sr
from pydub import AudioSegment
import io

def convert_audio(input_file, output_file):
    """deprecado - agora rodando em memoria"""
    audio = AudioSegment.from_ogg(input_file)
    audio.export(output_file, format="wav")

def transcribe_audio(audio_path):
    """deprecado - agora rodando em memoria"""
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)

    try:
        # Transcreve usando a API do Google
        transcricao = recognizer.recognize_google(audio_data, language='pt-BR')
        print(f'Transcrição do áudio: {transcricao}')
        return transcricao
    except sr.UnknownValueError:
        return "Não consegui entender o áudio."
    except sr.RequestError as e:
        return f"Erro ao conectar ao serviço de reconhecimento de fala: {e}"
    
def convert_audio_memoria(ogg_file):
    # Carrega o arquivo OGG em memória
    audio = AudioSegment.from_ogg(ogg_file)
    # Cria um buffer de memória para o arquivo WAV
    wav_file = io.BytesIO()
    audio.export(wav_file, format="wav")
    wav_file.seek(0)  # Volta o ponteiro do arquivo para o início
    return wav_file

def transcribe_audio_memoria(wav_file):
    recognizer = sr.Recognizer()

    with sr.AudioFile(wav_file) as source:
        audio_data = recognizer.record(source)

    try:
        # Transcreve usando a API do Google
        transcription = recognizer.recognize_google(audio_data, language='pt-BR')
        print(f'Transcrição do áudio: {transcription}')
        return transcription
    except sr.UnknownValueError:
        return "Não consegui entender o áudio."
    except sr.RequestError as e:
        return f"Erro ao conectar ao serviço de reconhecimento de fala: {e}"