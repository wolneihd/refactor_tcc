import requests

import os
from dotenv import load_dotenv

load_dotenv()
URL_API = os.getenv('URL_TELEGRAM')

def obter_dados_resposta(dados: dict):

    id_banco_dados = []
    id_usuario = ''

    for mensagem in dados.get('mensagens'):
        id_banco_dados.append(mensagem.get('id'))
        id_usuario = mensagem.get('usuario_id')
    
    resposta = dados.get('resposta')   

    obj = {
        'resposta': resposta,
        'usuario': id_usuario
    }
    response = requests.post(URL_API, json=obj)

    print("Status Code:", response.status_code)
    print("Resposta:", response.json())

    return id_banco_dados, resposta

if __name__ == "__main__":
    dados = {
    "mensagens": [{
            "analise_ia": "inconclusivel",
            "categoria": "outro",
            "feedback": "retorno incorreto",
            "id": 2,
            "llm": "GroqAI",
            "texto_msg": "Minha particular",
            "timestamp": 1736039772,
            "tipo_mensagem": "text",
            "usuario_id": 2,
            "checkbox": True
        }, {
            "analise_ia": "Positivo",
            "categoria": "atendimento",
            "feedback": "Atendimento de qualidade por Sérgio",
            "id": 3,
            "llm": "GroqAI",
            "texto_msg": "Queria informar que fui muito bem atendido pelo funcionário Sérgio.",
            "timestamp": 1739967139,
            "tipo_mensagem": "text",
            "usuario_id": 2,
            "checkbox": True
        }
    ],
    "resposta": "teste2222"
    }
    obter_dados_resposta(dados)