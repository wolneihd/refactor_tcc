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
    def __init__(self, data: dict, llm: str = None, transcription: str = None, n_imagem: str = None):

        if (data.content_type) == "text":

            print("Mensagem de TEXTO recebida:")
            self.id_user = data.from_user.id
            self.timestamp = data.date
            self.tipo_mensagem = data.content_type
            self.respondido = False
            self.texto_msg = data.json['text']
            self.imprimir_dados_nova_mensagem()
            self.analise_ia(llm=llm)

        elif (data.content_type) == "photo":

            print("Mensagem de IMAGEM recebida:")
            self.id_user = data.from_user.id
            self.timestamp = data.date
            self.tipo_mensagem = data.content_type
            self.respondido = False
            self.nome_imagem = n_imagem
            self.imprimir_dados_nova_mensagem() 

    def imprimir_dados_nova_mensagem(self):
        print(f"""mensagem do usuário: 
              \n id_user: {self.id_user} 
              \n timestamp: {self.timestamp} 
              \n tipo_mensagem: {self.tipo_mensagem}
              \n respondido: {self.respondido}
        """)

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
