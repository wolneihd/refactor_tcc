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
    def to_dict(mensagens: dict):
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
                'llm': mensagem['llm']
            }
            lista.append(dicionario)
        return lista
    