import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from openai import RateLimitError
from gerar_prompt import gerar_prompt

def analise_texto_chatgpt(mensagem: str):

    load_dotenv()
    OPEN_AI_KEY = os.getenv('OPENAI_API_KEY')
    OPENAI_MODEL = os.getenv('OPENAI_MODEL')

    llm = ChatOpenAI(
        model=OPENAI_MODEL,
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key=OPEN_AI_KEY,
    )

    prompt = gerar_prompt(mensagem=mensagem)

    messages = [
        ("system", "Você é um assistente que recebe um prompt de um agente e deve retornar conforme desejado"),
        ("human", prompt)
    ]
    try:
        response = llm.invoke(messages)
        print(response.content)
    except RateLimitError as error:
        if 'You exceeded your current quota' in str(error):
            return "A cota foi excedida. Por favor, verifique com o suporte ou entre no OpenAI e inclua saldo na sua conta."
    except Exception as error:
        return f'Erro ao enviar para análise do ChatGPT: {error}'

if __name__ == "__main__":
    analise = analise_texto_chatgpt('Eu não gostei do serviço!')
    print('Retorno IA: ', analise)