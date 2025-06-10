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

    # instanciando objeto:
    try:
        response = model.generate_content(prompt)        
        texto = response.text
        print('retorno IA: ', response.text)
        # texto = response.choices[0].message.content
        partes = texto.split(';')
        texto_formatado = [parte.replace('"', '').replace('.', '').replace('\n', '') for parte in partes]
        return texto_formatado[0], texto_formatado[1], texto_formatado[2]
    except Exception as error:
        if "You exceeded your current quota" in str(error):
            print(f"Limite de tokens atingido no Gemini")
        else: 
            print(f"Erro ao gerar Array e instanciar o objeto: {error}")            
        return None, None, None

if __name__ == "__main__":
    analise = analise_texto_gemini('Eu não gostei do serviço!')
    print('Retorno IA: ', analise)