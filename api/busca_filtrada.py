from datetime import datetime
from repository import select_filter

def filtrar_dados(dados: dict):

    # Dados para busca
    nome_sobrenome = dados.get('nome').capitalize()
    status = dados.get('status')
    llm_selecionada = dados.get('ia') 

    # converter para dados em busca no BD:
    if status == "em_aberto":
        status = 0
    elif status == "respondido":
        status = 1
    else:
        status = None

    if llm_selecionada == "groqia":
        llm_selecionada = 1
    elif llm_selecionada == "chatgpt":
        llm_selecionada = 2
    elif llm_selecionada == "gemini":
        llm_selecionada = 3
    else:
        llm_selecionada = None

    # Dados da busca convertidos:
    print(f"""
          Buscando:
          nome: {nome_sobrenome}
          status: {status}
          llm da busca: {llm_selecionada}
          """, flush=True)

    pessoas = select_filter(
         nome = nome_sobrenome,
         status = status,
         llm_selecionada = llm_selecionada
    )

    return pessoas

    # {
    #             'id': mensagem.get('id'),
    #             'usuario_id': mensagem.get('usuario_id'),
    #             'texto_msg': mensagem.get('texto_msg'),
    #             'timestamp': mensagem.get('timestamp'),
    #             'tipo_mensagem': mensagem.get('tipo_mensagem'),
    #             'analise_ia': mensagem.get('analise_ia'),
    #             'categoria': mensagem.get('categoria'),
    #             'feedback': mensagem.get('feedback'),
    #             'llm': mensagem.get('llm_id'),
    #             'respondido': mensagem.get('respondido'),
    #             'nome_arquivo': mensagem.get('nome_imagem')
    #         }

    # status = dados.get('status') # 0 em aberto / 1 respondido    
    # llm_selecionada = dados.get('ia')    

    # nome_sobrenome = dados.get('nome')
    # analise_ia = dados.get('analise_ia') # positivo, neutro, negativo
    # categoria = dados.get('categoria')   # palavra chave
    # data_de = dados.get('dataDe')
    # data_ate = dados.get('DataAte')
    # llm_selecionada = dados.get('ia')
    # tipo = dados.get('tipo')
    # categoria = dados.get('categoria')

    # conversão para Timestamp para poder fazer busca no banco de dados:
    # try:
    #     data_de_obj = datetime.strptime(data_de, '%Y-%m-%d')
    #     data_ate_obj = datetime.strptime(data_ate, '%Y-%m-%d')
    #     timestamp_data_de = data_de_obj.timestamp()
    #     timestamp_data_ate = data_ate_obj.timestamp()
    # except Exception as e:
    #     timestamp_data_de = False
    #     timestamp_data_ate = False
    #     print('Não foi possível obter datas')

    # if analise_ia not in ["positivo", "neutro", "negativo"]:
    #     analise_ia == None

    # if categoria not in ["limpeza", "organizacao", "atendimento", "pedido", "outros"]:
    #     categoria == None

    # if llm_selecionada == "groqia":
    #     llm_selecionada = 1
    # elif llm_selecionada == "chatgpt":
    #     llm_selecionada = 2
    # elif llm_selecionada == "gemini":
    #     llm_selecionada = 3

    # if status == "em_aberto":
    #     status = 0
    # elif status == "respondido":
    #     status = 1
    # else:
    #     status = None
    
    # select_filter(
    #     status=status,
    #     llm_selecionada=llm_selecionada
    # )


