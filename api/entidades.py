from get_url_minio import get_url

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
                'id': mensagem.get('id'),
                'usuario_id': mensagem.get('usuario_id'),
                'texto_msg': mensagem.get('texto_msg'),
                'timestamp': mensagem.get('timestamp'),
                'tipo_mensagem': mensagem.get('tipo_mensagem'),
                'analise_ia': mensagem.get('analise_ia'),
                'categoria': mensagem.get('categoria'),
                'feedback': mensagem.get('feedback'),
                'llm': mensagem.get('llm_id'),
                'respondido': mensagem.get('respondido'),
                'nome_arquivo': mensagem.get('nome_imagem')
            }

            # if dicionario.get('tipo_mensagem') == "photo":
            #     dicionario['url'] = get_url(dicionario.get('nome_arquivo'))

            lista.append(dicionario)

        return lista
    