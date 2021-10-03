def cadastrar_clientes(nome,cpf,):
    arquivo_dados = open('dados.txt', 'r')
    cont = 0
    for linha in arquivo_dados:
        dados = linha.split()
        if int(dados[0]) == 1:
            if int(dados[2]) == (cpf):
                cont += 1
    arquivo_dados.close()
    if cont == 1:
        print('cpf ja cadastado')
    else:
        arquivo_dados = open('dados.txt', 'a')
        arquivo_dados.write(f'1 {nome} {cpf}\n')
        arquivo_dados.close()
def cadastrar_maquina(codigo,maquina,marca,modelo,ano,valor,status):
    contador = 0

    arquivo_dados = open('dados.txt','r')
    for linha in arquivo_dados:
        dados = linha.split()
        if int(dados[0]) == 2:
            contador += 1
        if contador == 3:
            break
    arquivo_dados.close()
    if contador < 3:
        arquivo_dados = open('dados.txt','a')
        arquivo_dados.write(f'2 {codigo} {maquina} {marca} {modelo} {ano} {valor} {status}\n')
            
            
