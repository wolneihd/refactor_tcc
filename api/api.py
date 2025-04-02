from flask import Flask, jsonify, request
from flask_cors import CORS
from repository import select_all_mensagens, buscar_todas_llms, atualizar_ia
from repository import create_tables, insert_feedback_totem, atualizar_resposta_bd, buscar_mensagens_totem
from gerar_resposta import gerar_resposta_ia
from enviar_resposta import obter_dados_resposta
from busca_filtrada import filtrar_dados
from service_usuarios import service_buscar_usuarios

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
    
    # obter todas as mensagens:
    @app.route('/filtrar', methods=['POST'])
    def filtrar_mensagens():
        dados = request.get_json()
        filtrar_dados(dados)
        return jsonify({"retorno":"com sucesso no backend!"})  

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

    # obter todas as mensagens:
    @app.route('/totem', methods=['GET'])
    def quantidades_totem():
        data = buscar_mensagens_totem()
        return jsonify(data)

    # obter todas os usuarios:
    @app.route('/usuarios', methods=['GET'])
    def obter_todos_usuarios():
        data = service_buscar_usuarios()
        return jsonify(data) 
    
    # obter todas as LLMS:
    @app.route('/llm-disponivel', methods=['GET'])
    def obter_todas_opcoes_llm():
        data = buscar_todas_llms()
        return jsonify(data)

    # salvar IA alterada:
    @app.route('/alterar-ia', methods=['POST'])
    def salvar_ia():
        dados = request.get_json()
        atualizar_ia(dados.get('ia'))

        print(dados.get('ia'), flush=True)
        print(dados.get('chave'), flush=True)
        print(dados.get('powerbi'), flush=True)
        return jsonify({'retorno': "teste"}) 

    app.run(port=PORT,host=HOST,debug=True)

if __name__ == "__main__":
    create_tables()
    montar_API()