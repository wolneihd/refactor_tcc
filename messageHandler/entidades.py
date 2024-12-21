from groqIA import analise_texto_gropIA
from geminiAI import analise_texto_gemini
from chatGPT import analise_texto_chatgpt

class User:
    def __init__(self, user):  
        self.userID_Telegram = user.id  
        self.nome = user.first_name  
        self.sobrenome = user.last_name if user.last_name else ''  

class Message:
    def __init__(self, data: dict, configs: dict):
        self.id_user = data.from_user.id
        self.texto_msg = data.json['text']  
        self.timestamp = data.date
        self.tipo_mensagem = data.content_type
        self.analise_ia(configs=configs)

    def analise_ia(self, configs: dict):

        for config in configs:
            if config['campo'] == 'llm':
                llm = config['valor']

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
