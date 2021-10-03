try:
    f = open('dados.txt')
    f.close()
except:
    f = open('dados.txt','a')
    f.close()




    arquivo_dados.close()



escolha = 1
while escolha != 0:
    print('Escolha uma opção do menu:')
    print()
    print('1 - Cadastrar cliente')
    print('2 - Cadastrar maquina')
    print('3 - Registro de aluguel')
    print('4 - Relatorio de clientes')
    print('5 - Relatorio de maquinas')
    print('6 - Relatório de Reservas')
    print('0 - Sair')
    print()
    escolha = int(input('escolha sua opção: '))

    if escolha == 1:
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
            

        
