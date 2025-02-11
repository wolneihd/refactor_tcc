from flask import Flask, jsonify, request
from flask_cors import CORS
from repository import select_all_mensagens
from repository import create_tables, insert_feedback_totem

def montar_API():
    # motando API
    app = Flask(__name__)
    CORS(app)

    # obter todas as mensagens:
    @app.route('/', methods=['GET'])
    def todas_mensagens():
        data = select_all_mensagens()  
        return jsonify(data)  
    
    # responder mensagem do usuário:
    @app.route('/responder', methods=['POST'])
    def responder_mensagens():
        return jsonify({'teste': [1,2]})  
    
    # salvar mensagem do totem de feedback:
    @app.route('/totem', methods=['POST'])
    def salvar_mensagem():
        # Obter dados do corpo da requisição
        dados = request.get_json()
        insert_feedback_totem(status_totem=dados.get('status'))
        return jsonify({'teste': [1,2]})  

    app.run(port=5000,host="0.0.0.0",debug=True)

if __name__ == "__main__":
    create_tables()
    montar_API()