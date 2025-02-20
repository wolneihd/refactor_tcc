from flask import Flask, jsonify, request
from flask_cors import CORS
from repository import select_all_mensagens
from repository import create_tables, insert_feedback_totem, atualizar_resposta_bd
from gerar_resposta import gerar_resposta_ia
from enviar_resposta import obter_dados_resposta

import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv('API_HOST')
PORT = int(os.getenv('API_PORT'))

def montar_API():
    # motando API
    app = Flask(__name__)
    CORS(app)

    # obter todas as mensagens:
    @app.route('/', methods=['GET'])
    def todas_mensagens():
        data = select_all_mensagens()  
        return jsonify(data)  
    
    # gerar sugestão resposta com IA:
    @app.route('/gerar_resposta', methods=['POST'])
    def gerar_resposta():
        dados = request.get_json()
        retorno = gerar_resposta_ia(dados)
        return jsonify({'resposta': retorno})  
        # return jsonify({'resposta': 'teste'})  
    
    # responder mensagem do usuário:
    @app.route('/responder', methods=['POST'])
    def responder_mensagens():
        dados = request.get_json()
        ids, resposta = obter_dados_resposta(dados)
        atualizar_resposta_bd(ids, resposta)
        return jsonify({'dados': dados})  
    
    # salvar mensagem do totem de feedback:
    @app.route('/totem', methods=['POST'])
    def salvar_mensagem():
        # Obter dados do corpo da requisição
        dados = request.get_json()
        retorno = insert_feedback_totem(status_totem=dados.get('status'))
        return jsonify({'retorno': retorno})  

    app.run(port=PORT,host=HOST,debug=True)

if __name__ == "__main__":
    create_tables()
    montar_API()