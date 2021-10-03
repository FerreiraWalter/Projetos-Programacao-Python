def alterar_linha(path,codigo,nova_linha):
    with open(path,'r') as f:
        texto=f.readlines()
    with open(path,'w') as f:
        for i in texto:
            if codigo in i:
                f.write(nova_linha+'\n')
            else:
                f.write(i)
                
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