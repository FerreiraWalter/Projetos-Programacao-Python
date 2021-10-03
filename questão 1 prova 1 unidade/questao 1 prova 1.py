from funcoes import *
try:
    f = open('dados.txt')
    f.close()
except:
    f = open('dados.txt','a')
    f.close()




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


