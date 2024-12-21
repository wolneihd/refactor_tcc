from groqIA import analise_texto_gropIA

class User:
    def __init__(self, user):  
        self.userID_Telegram = user.id  
        self.nome = user.first_name  
        self.sobrenome = user.last_name if user.last_name else ''  

class Message:
    def __init__(self, data: dict):
        self.id_user = data.from_user.id
        self.texto_msg = data.json['text']  
        self.timestamp = data.date
        self.tipo_mensagem = data.content_type
        self.analise_ia()

    def analise_ia(self):
        analiseIA, categoria, feedback = analise_texto_gropIA(self.texto_msg)
        self.analiseIA = analiseIA
        self.categoria = categoria
        self.feedback = feedback