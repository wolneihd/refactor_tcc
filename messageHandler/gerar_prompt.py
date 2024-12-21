def gerar_prompt(mensagem: str) -> str:
    texto = f"""
        - você deve analisar a mensagem enviada abaixo.
        - serão 03 respostas que devem ser separadas por ; entre elas para podemos depois podermos tabular os dados.
        - pergunta 01: foi um feedback - positivo, negativo, neutro ou inconclusivel?
        - pergunta 02: categorizar (somente uma opção válida): limpeza, organização, atendimento, outro.
        - pergunta 03: resumir em até no máximo 50 caracteres (considerando pontuações e espaços vazios). 

        Feedback do usuário: {mensagem}. 

        O retorno do assistente deve ser apenas: 

        resposta01;resposta02;resposta03
        """
    return texto

if __name__ == "__main__":
    prompt = gerar_prompt('Eu não gostei do serviço!')
    print(prompt)