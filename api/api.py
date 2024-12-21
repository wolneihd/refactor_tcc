from flask import Flask, jsonify
from flask_cors import CORS
from reporitory import select_all_mensagens

def montar_API():
    # motando API
    app = Flask(__name__)
    CORS(app)

    # consultar todas capitais:
    @app.route('/', methods=['GET'])
    def todas_mensagens():
        data = select_all_mensagens()  
        return jsonify(data)  
    
    app.run(port=5001,host='localhost',debug=True)

if __name__ == "__main__":
    montar_API()