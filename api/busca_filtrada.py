from datetime import datetime
from repository import select_filter

def filtrar_dados(dados: dict):

    print(f"dados: {dados}", flush=True)

    nome_sobrenome = dados.get('nome')
    analise_ia = dados.get('analise_ia') # positivo, neutro, negativo
    categoria = dados.get('categoria')   # palavra chave
    data_de = dados.get('dataDe')
    data_ate = dados.get('DataAte')
    llm_selecionada = dados.get('ia')
    status = dados.get('status') # 0 em aberto / 1 respondido
    tipo = dados.get('tipo')
    categoria = dados.get('categoria')

    # conversão para Timestamp para poder fazer busca no banco de dados:
    data_de_obj = datetime.strptime(data_de, '%Y-%m-%d')
    data_ate_obj = datetime.strptime(data_ate, '%Y-%m-%d')
    timestamp_data_de = data_de_obj.timestamp()
    timestamp_data_ate = data_ate_obj.timestamp()

    if analise_ia not in ["positivo", "neutro", "negativo"]:
        analise_ia == None

    if categoria not in ["limpeza", "organizacao", "atendimento", "pedido", "outros"]:
        categoria == None

    if llm_selecionada == "groqia":
        llm_selecionada = 1
    elif llm_selecionada == "chatgpt":
        llm_selecionada = 2
    elif llm_selecionada == "gemini":
        llm_selecionada = 3

    if status == "em_aberto":
        status = 0
    elif status == "respondido":
        status = 1
    else:
        status = None

    print(
        f"analise_ia={analise_ia}",
        f"status={status}",
        f"timestamp_data_de={timestamp_data_de}",
        f"timestamp_data_ate={timestamp_data_ate}",
        f"nome_sobrenome={nome_sobrenome}",
        f"categoria={categoria}",
        f"llm_selecionada={llm_selecionada}",
        f"tipo={tipo}",
        flush=True
    )

    select_filter(
        analise_ia=analise_ia,
        status=status,
        tipo=tipo
    )
    


