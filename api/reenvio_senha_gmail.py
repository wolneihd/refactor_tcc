import smtplib
import email.message

import os
from dotenv import load_dotenv

load_dotenv()
EMAIL = os.getenv('EMAIL')
SENHA = os.getenv('SENHA_GOOGLE')

def enviar_email(destinatario: str):
    try:
        print('Enviando e-mail...', flush=True)

        with open('email_padrao.html', 'r', encoding='utf-8') as f:
            conteudo = f.read()        

        msg = email.message.Message()
        msg['Subject'] = 'Reset da senha da aplicação Eai?'
        msg['From'] = EMAIL
        msg['To'] = destinatario

        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(conteudo)

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()

        s.login(msg['From'], password=SENHA)
        s.sendmail(msg['FROM'], [msg['To']], msg.as_string().encode('utf-8'))

        print(f'Email enviado com sucesso para: {destinatario}', flush=True)
    except Exception as error:
         print(f'Erro ao enviar mensagem a pessoa: {destinatario}', flush=True)

