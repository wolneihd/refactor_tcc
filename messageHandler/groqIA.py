import os
from groq import Groq
from dotenv import load_dotenv

def analise_texto_gropIA(mensagem: str):
    # Create the Groq client
    load_dotenv()
    GROQ_API_KEY = os.getenv('GROQ_API_KEY')
    client = Groq(api_key=os.environ.get(GROQ_API_KEY), )

    # Set the system prompt
    system_prompt = {
        "role": "system",
        "content": "Você atua como um assistente que analisa a feedbacks enviados por clients via bot do Telegrama."
    }

    # Initialize the chat history
    chat_history = [system_prompt]

    # Get user input from the console
    user_input = f"""
    - você deve analisar a mensagem enviada abaixo.
    - serão 03 respostas que devem ser separadas por ; entre elas para podemos depois podermos tabular os dados.
    - pergunta 01: foi um feedback - positivo, negativo, neutro ou inconclusivel?
    - pergunta 02: categorizar (somente uma opção válida): limpeza, organização, atendimento, outro.
    - pergunta 03: resumir em até no máximo 50 caracteres (considerando pontuações e espaços vazios). 

    Feedback do usuário: {mensagem}. 

    O retorno do assistente deve ser apenas: 
    
    resposta01;resposta02;resposta03
    """
    # Append the user input to the chat history
    chat_history.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(model="llama3-70b-8192",
                                                messages=chat_history,
                                                max_tokens=100,
                                                temperature=1.2)

    # Append the response to the chat history
    chat_history.append({
          "role": "assistant",
          "content": response.choices[0].message.content
      })

    # instanciando objeto:
    try:
        print('retorno IA: ', response.choices[0].message.content)
        texto = response.choices[0].message.content
        partes = texto.split(';')
        texto_formatado = [parte.replace('"', '').replace('.', '') for parte in partes]
        return texto_formatado[0], texto_formatado[1], texto_formatado[2]
    except:
        print("Erro ao gerar Array e instanciar o objeto.")
        return None, None, None
    

    