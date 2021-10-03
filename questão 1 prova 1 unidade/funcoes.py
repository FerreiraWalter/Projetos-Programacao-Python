def cadastrar_clientes(nome,cpf,arquivo):
    dados = open(f'{arquivo}.txt','a')
    for linha in dados:
        