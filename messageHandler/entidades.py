from groqIA import analise_texto_gropIA
from geminiAI import analise_texto_gemini
from chatGPT import analise_texto_chatgpt

class User:
    def __init__(self, user):  
        self.userID_Telegram = user.id  
        self.nome = user.first_name  
        self.sobrenome = user.last_name if user.last_name else ''  

class Message:
    def __init__(self, data: dict, llm: str, transcription: str = None):
        self.id_user = data.from_user.id
        self.timestamp = data.date
        self.tipo_mensagem = data.content_type
        self.respondido = False

        if transcription == None:
            self.texto_msg = data.json['text']  
        else:
            self.texto_msg = transcription

        self.analise_ia(llm=llm)

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
