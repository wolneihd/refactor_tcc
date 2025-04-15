from repository import salvar_novo_usuario, buscar_todos_usuarios

def service_buscar_usuarios():
    data = buscar_todos_usuarios()
    return data

def service_salvar_usuario(nome: str, email: str):
    response = salvar_novo_usuario(nome, email)
    return response
