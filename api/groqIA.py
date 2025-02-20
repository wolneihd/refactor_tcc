import os
from groq import Groq
from dotenv import load_dotenv

def analise_texto_gropIA(prompt: list):

    load_dotenv()
    GROQ_API_KEY = os.getenv('GROQ_API_KEY')
    client = Groq(api_key=os.environ.get(GROQ_API_KEY), )

    chat_history = [{"role": "assistant", "content": prompt}]

    response = client.chat.completions.create(model="llama3-70b-8192",
                                                messages=chat_history,
                                                temperature=.5)

    return response.choices[0].message.content



    

    