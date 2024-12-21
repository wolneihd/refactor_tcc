from dotenv import load_dotenv
import os
import google.generativeai as genai
from gerar_prompt import gerar_prompt

def analise_texto_gemini(mensagem: str):

    load_dotenv()
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    MODEL = os.getenv('GEMINI_MODEL')

    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel(MODEL)

    prompt = gerar_prompt(mensagem)

    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    analise = analise_texto_gemini('Eu não gostei do serviço!')
    print('Retorno IA: ', analise)