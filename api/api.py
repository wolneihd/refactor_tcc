from flask import Flask, jsonify
from flask_cors import CORS
from repository import select_all_mensagens

def montar_API():
    # motando API
    app = Flask(__name__)
    CORS(app)

    # consultar todas capitais:
    @app.route('/', methods=['GET'])
    def todas_mensagens():
        data = select_all_mensagens()  
        return jsonify(data)  
    
    # consultar todas capitais:
    @app.route('/responder', methods=['POST'])
    def responder_mensagens():
        return jsonify({'teste': [1,2]})  

    app.run(port=5001,host='localhost',debug=True)

if __name__ == "__main__":
    montar_API()