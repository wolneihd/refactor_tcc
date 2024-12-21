class User:
    def to_dict(usuarios):
        lista = []
        for usuario in usuarios:
            dicionario = {
                'id': usuario['id'],
                'nome': usuario['nome'],
                'sobrenome': usuario['sobrenome'],
                'userID_Telegram': usuario['userID_Telegram'],
                'mensagens': []
            }
            lista.append(dicionario)
        return lista
    
class Message:
    def __init__(self):
        pass

    def compare_id(self, llms: dict, id: int):
        for dado in llms:
            if dado['id'] == id:
                return dado['llm']

    def to_dict(self, mensagens: dict, llms: dict):
        lista = []
        for mensagem in mensagens:
            dicionario = {
                'id': mensagem['id'],
                'usuario_id': mensagem['usuario_id'],
                'texto_msg': mensagem['texto_msg'],
                'timestamp': mensagem['timestamp'],
                'tipo_mensagem': mensagem['tipo_mensagem'],
                'analise_ia': mensagem['analise_ia'],
                'categoria': mensagem['categoria'],
                'feedback': mensagem['feedback'],
                'llm': self.compare_id(llms=llms, id=mensagem['llm_id']),
            }
            lista.append(dicionario)
        return lista
    