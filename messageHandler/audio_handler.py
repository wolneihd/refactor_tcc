import speech_recognition as sr
from pydub import AudioSegment

def convert_audio(input_file, output_file):
    audio = AudioSegment.from_ogg(input_file)
    audio.export(output_file, format="wav")

def transcribe_audio(audio_path):
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