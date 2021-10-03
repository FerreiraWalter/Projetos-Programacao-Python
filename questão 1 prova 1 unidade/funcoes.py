def cadastrar_clientes(nome,cpf,arquivo):
    arquivo_dados = open(f'{arquivo}.txt','a')
    cont = 0
    for linha in arquivo_dados:
        dados = linha.split()
        if dados[2] == cpf:
            cont += 1
    


