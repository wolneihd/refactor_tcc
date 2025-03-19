import pprint
from groqIA import analise_texto_gropIA
from geminiAI import analise_texto_gemini
from chatGPT import analise_texto_chatgpt

class User:
    def __init__(self, user):  
        self.userID_Telegram = user.id  
        self.nome = user.first_name  
        self.sobrenome = user.last_name if user.last_name else ''  
        self.__imprimir_usuario__()

    def __imprimir_usuario__(self):
        print(f"mensagem do usuário: \nid: {self.userID_Telegram} \nNome: {self.nome} \nSobrenome: {self.sobrenome}")

class Message:
    def __init__(self, data: dict, llm: str = None, transcription: str = None, n_imagem: str = None, n_audio: str = None):

        if (data.content_type) == "text":

            print("Mensagem de TEXTO recebida:")
            self.id_user = data.from_user.id
            self.timestamp = data.date
            self.tipo_mensagem = data.content_type
            self.respondido = False
            self.texto_msg = data.json['text']
            self.analise_ia(llm=llm)

        elif (data.content_type) == "photo":

            print("Mensagem de IMAGEM recebida:")
            self.id_user = data.from_user.id
            self.timestamp = data.date
            self.tipo_mensagem = data.content_type
            self.respondido = False
            self.nome_imagem = n_imagem

        elif (data.content_type) == "voice":

            print("Mensagem de Audio recebida:", flush=True)
            self.id_user = data.from_user.id
            self.timestamp = data.date
            self.tipo_mensagem = data.content_type
            self.respondido = False
            self.nome_audio = n_audio
            self.texto_msg = transcription
            self.analiseIA = None
            self.categoria = None
            self.feedback = None
            self.analise_ia(llm)  
            self.__imprimir_msg_audio()  

    def __imprimir_msg_audio(self):
        print(f"""
            id_user = {self.id_user}
            timestamp = {self.timestamp}
            tipo_mensagem = {self.tipo_mensagem}
            respondido = {self.respondido}
            nome_audio = {self.nome_audio}
            transcricao = {self.texto_msg}
            analiseIA = {self.analiseIA}
            categoria = {self.categoria}
            feedback = {self.feedback}
            """, flush=True)       

    def analise_ia(self, llm: str):

        if llm == 'GroqAI':
            analiseIA, categoria, feedback = analise_texto_gropIA(self.texto_msg)
        elif llm == 'ChatGPT':
            analiseIA, categoria, feedback = analise_texto_chatgpt(self.texto_msg)
        elif llm == 'Gemini':
            analiseIA, categoria, feedback = analise_texto_gemini(self.texto_msg)

        self.llm = llm
        self.analiseIA = analiseIA
        self.categoria = categoria
        self.feedback = feedback
        self.resposta = None
