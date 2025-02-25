from groqIA import analise_texto_gropIA

def gerar_resposta_ia(dados: dict):

    # criar array com todas as mensagens:
    mensagens = []
    for mensagem in dados.get('mensagens'):
        mensagens.append(mensagem.get('texto_msg'))

    # criar prompt para AI:
    prompt = f"""
        Você é um assistente virtual que analisa um grupo de mensagens e com um contexto adicional do usuário gera uma resposta amigável de retorno a um cliente.
        Objetivo principal é agradecer o envio da mensagem e indicar que estaremos analisando.
        
        Lista de mensagens: {str(mensagens)}

        Contexto adicional do usuário: '''{dados.get('texto_adicional')}'''
        Caso o contexto adicional venha vazio, gerar uma resposta apenas considerando o contexto já dado.
        Você deve inserir obrigatoriamente o contexto adicional.

        O seu retorno deve ser apenas a mensagem para o cliente.
        Remover as quebras de linha antes do inicio do texto.
    """

    resposta = analise_texto_gropIA(prompt=prompt)
    return resposta

if __name__ == "__main__":
    retorno = {
        "texto_adicional": "",
        "mensagens": [{
                "analise_ia": "inconclusivel",
                "categoria": "outro",
                "feedback": "mensagem sem conteúdo",
                "id": 1,
                "llm": "GroqAI",
                "texto_msg": "Minha mensagem",
                "timestamp": 1736039759,
                "tipo_mensagem": "text",
                "usuario_id": 1,
                "checkbox": True
            }
        ]
    }
    gerar_resposta_ia(retorno)