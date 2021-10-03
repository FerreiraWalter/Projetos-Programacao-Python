def cadastrar_clientes(nome,cpf,):
    cpf = str(input('Digite o cpf do cliente: '))
    nome = str(input('Digite o nome do cliente: '))
    arquivo_dados = open('dados.txt', 'r')
    cont = 0
    for linha in arquivo_dados:
        dados = linha.split()
        if dados[2] == cpf:
            cont += 1
    arquivo_dados.close()
    if cont == 1:
        print('cpf ja cadastado')
    else:
        arquivo_dados = open('dados.txt', 'a')
        arquivo_dados.write(f'1 {nome} {cpf}')
        arquivo_dados.close()



