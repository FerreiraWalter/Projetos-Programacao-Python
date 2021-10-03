def cadastrar_clientes(nome,cpf):
    arquivo_dados = open('dados_pessoas.txt', 'r')
    cont = 0
    for linha in arquivo_dados:
        dados = linha.split()
        if int(dados[1]) == (cpf):
            cont += 1
    arquivo_dados.close()
    if cont == 1:
        print('cpf ja cadastado')
    else:
        arquivo_dados = open('dados_maquinas.txt', 'a')
        arquivo_dados.write(f'{nome} {cpf}\n')
        arquivo_dados.close()
def cadastrar_maquina(codigo,tipo,marca,modelo,ano,valor,status):
    contador = 0
    arquivo_dados = open('dados.txt','r')
    for linha in arquivo_dados:
        dados = linha.split()
        contador += 1
        if contador == 3:
            break
    arquivo_dados.close()
    if contador < 3:
        arquivo_dados = open('dados.txt','a')
        arquivo_dados.write(f'{codigo} {tipo} {marca} {modelo} {ano} {valor} {status}\n')
    else:
        print('o limite de maquinas ja foi atingido')
            
def reservar_maquina(cpf,codigo):
    arquivo_maquinas = open('dados_maquinas.txt''+')
    arquivo_pessoas = open('dados_pessoas.txt','+')
    for linha in arquivo_pessoas:
        dados = linha.split()
        for n in arquivo_maquinas:
            dados2 = n.split()
            if dados2[]

