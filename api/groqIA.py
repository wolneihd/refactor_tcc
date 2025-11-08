import os
from groq import Groq
from dotenv import load_dotenv

def analise_texto_gropIA(prompt: str):

    try:
        load_dotenv()
        GROQ_API_KEY = os.getenv('GROQ_API_KEY')
        client = Groq(api_key=os.environ.get(GROQ_API_KEY), )

        chat_history = [{"role": "assistant", "content": prompt}]

        response = client.chat.completions.create(model="meta-llama/llama-4-maverick-17b-128e-instruct",
                                                    messages=chat_history,
                                                    temperature=1)

        print(f'Response: {response}', flush=True)

        return response.choices[0].message.content
    except Exception as error:
        return error

def reanalise_texto_gropIA(prompt: str):

    try:
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
    
        # Append the user input to the chat history
        chat_history.append({"role": "user", "content": prompt})

        response = client.chat.completions.create(model="llama3-70b-8192",
                                                    messages=chat_history,
                                                    max_tokens=100,
                                                    temperature=1.2)

        # Append the response to the chat history
        chat_history.append({
              "role": "assistant",
              "content": response.choices[0].message.content
          })

        print('retorno IA: ', response.choices[0].message.content)
        texto = response.choices[0].message.content
        partes = texto.split(';')
        texto_formatado = [parte.replace('"', '').replace('.', '') for parte in partes]
        return texto_formatado[0], texto_formatado[1], texto_formatado[2]
    except Exception as error:
        print(f"Erro ao gerar Array e instanciar o objeto: {error}")
        return None, None, None


    

    