from groqIA import analise_texto_gropIA, reanalise_texto_gropIA

def gerar_resposta_ia(dados: dict):
    try:
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
            Caso o contexto adicional venha vazio, gerar uma resposta apenas considerando a lista de mensagens.
            Você deve considerar obrigatoriamente o contexto adicional para gerar sua resposta.

            Gerar uma resposta amigável. Evitar ser muito sucinto.
            Remover as quebras de linha antes do inicio do texto.
        """

        print(f'Seu prompt: {prompt}', flush=True)
        resposta = analise_texto_gropIA(prompt=prompt)
        return resposta
    except Exception as error:
        print(f'Erro ao gerar resposta: {error}', flush=True)
        return error
    
def reprocessar_mensagem_usuario(dados: dict) -> dict:  

    id = dados.get('id')
    texto = dados.get('mensagem')

    # criar prompt para AI:
    prompt = f"""
        - você deve analisar a mensagem enviada abaixo.
        - serão 03 respostas que devem ser separadas por ; entre elas para podemos depois podermos tabular os dados.
        - pergunta 01: foi um feedback - positivo, negativo, neutro ou inconclusivel?
        - pergunta 02: categorizar (somente uma opção válida): limpeza, organização, atendimento, outro.
        - pergunta 03: resumir em até no máximo 50 caracteres (considerando pontuações e espaços vazios). 

        Feedback do usuário: {texto}. 

        O retorno do assistente deve ser apenas: 

        resposta01;resposta02;resposta03
        """
    feedback, categoria, resumo = reanalise_texto_gropIA(prompt)
    return {
        'feedback': feedback,
        'categoria': categoria,
        'resumo': resumo
    }

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