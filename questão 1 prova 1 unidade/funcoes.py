def cadastrar_clientes(nome,cpf):
    arquivo_dados = open('dados_pessoas.txt', 'r')
    cont = 0
    for linha in arquivo_dados:
        dados = linha.split()
        if len(dados) > 0:
            if int(dados[1]) == (cpf):
                cont += 1
    arquivo_dados.close()
    if cont == 1:
        print('cpf ja cadastado')
    else:
        arquivo_dados = open('dados_pessoas.txt', 'a')
        arquivo_dados.write(f'{nome} {cpf}\n')
        arquivo_dados.close()
def cadastrar_maquina(codigo,tipo,marca,modelo,ano,valor,status):
    contador = 0
    arquivo_dados = open('dados_maquinas.txt','r')
    for linha in arquivo_dados:
        dados = linha.split()
        contador += 1
        if contador == 3:
            break
    arquivo_dados.close()
    if contador < 3:
        arquivo_dados = open('dados_maquinas.txt','a')
        arquivo_dados.write(f'{codigo} {tipo} {marca} {modelo} {ano} {valor} {status}\n')
    else:
        print('o limite de maquinas ja foi atingido')
            
def reservar_maquina(cpf,codigo):
    cont_maquinas = -1
    cont_pessoas = -1
    dados_temp_maquinas = []
    dados_temp_pessoas = []
    arquivo_maquinas = open('dados_maquinas.txt', 'r')
    cont = 0
    for n in arquivo_maquinas:
        dados2 = n.split()
        cont_maquinas += 1

        dados_temp_maquinas.append(
            f'{dados2[0]} {dados2[1]} {dados2[2]} {dados2[3]} {dados2[4]} {dados2[5]} {dados2[6]}\n')
        arquivo_pessoas = open('dados_pessoas.txt', 'r')
        cont += 1
        for linha in arquivo_pessoas:
            dados = linha.split()
            if cont == 1:
                try:
                    dados_temp_pessoas.append(f'{dados[0]} {dados[1]} {dados[2]}\n')
                    cont_pessoas += 1
                except:
                    dados_temp_pessoas.append(f'{dados[0]} {dados[1]}\n')
                    cont_pessoas += 1
            if int(dados2[6]) == 1:
                if int(dados2[0]) == int(codigo) and int(dados[1]) == int(cpf):
                    dados_temp_maquinas[
                        cont_maquinas] = f'{dados2[0]} {dados2[1]} {dados2[2]} {dados2[3]} {dados2[4]} {dados2[5]} 2\n'
                    dados_temp_pessoas[cont_pessoas] = (f'{dados[0]} {dados[1]} {dados2[0]}\n')
    arquivo_maquinas.close()
    arquivo_pessoas.close()
    arquivo_dados = open('dados_maquinas.txt', 'w')
    for n in dados_temp_maquinas:
        arquivo_dados.write(n)
    arquivo_dados.close()
    arquivo_dados = open('dados_pessoas.txt', 'w')
    for n in dados_temp_pessoas:
        arquivo_dados.write(n)
    arquivo_dados.close()



