from datetime import datetime
from repository import select_filter

def filtrar_dados(dados: dict):

    # recebido frontend:
    print(f'{dados}', flush=True)

    # Dados para busca
    nome_sobrenome = dados.get('nome').capitalize()
    status = dados.get('status')
    llm_selecionada = dados.get('ia') 
    analise_ia = dados.get('analise_ia')
    categoria = dados.get('categoria')
    tipo_mensagem = dados.get('tipo')
    data_de = dados.get('dataDe')
    data_ate = dados.get('DataAte')        

    # converter da data para datetime:
    if (data_de):
        dt_de = datetime.strptime(data_de, '%Y-%m-%d').timestamp()
    else: 
        dt_de = None

    if (data_ate):
        dt_ate = datetime.strptime(data_ate, '%Y-%m-%d').timestamp()
    else: 
        dt_ate = None

    # regra tipo de mensagem
    if tipo_mensagem == 'todas':
        tipo_mensagem = None

    # criar regra para analise-ia:
    if analise_ia == 'todas':
        analise_ia = None

    # criar regra para analise-ia:
    if categoria == 'todas':
        categoria = None
    else: 
        categoria = categoria.lower()

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
        status (em_aberto/respondido): {status}
        llm da busca: {llm_selecionada}
        analise_ia: {analise_ia}
        categoria: {categoria}
        tipo_mensagem: {tipo_mensagem}
        data_de: {data_de} - {dt_de}
        data_ate: {data_ate} - {dt_ate}
    """, flush=True)

    pessoas = select_filter(
         nome = nome_sobrenome,
         status = status,
         llm_selecionada = llm_selecionada,
         analise_ia=analise_ia,
         categoria=categoria,
         tipo=tipo_mensagem,
         timestamp_data_de=dt_de,
         timestamp_data_ate=dt_ate
    )

    return pessoas
