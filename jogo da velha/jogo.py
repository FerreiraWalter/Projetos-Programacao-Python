import os

from random import choice

def gerar_vitorias(nome_arquivo):
    vitorias = []
    arquivo = open(f'{nome_arquivo}.txt','r')
    for n in arquivo:
        vitorias.append([])
        for c in n:
            if c.isnumeric() == True:
                vitorias[len(vitorias)-1].append(int(c))
    return vitorias

def consultar_vitoria(matriz,jogo):
    pontos_X = 0 #1
    pontos_0 = 0 #2
    for n in range(len(matriz)):
        if pontos_X < 3 :
            if pontos_0 <3:
                pontos_X = 0 #1
                pontos_0 = 0 #2
                for c in range(len(matriz[n])):
                    if pontos_X < 3 :
                        if pontos_0 <3:
                            if matriz[n][c] == 1 and jogo[c] == 'X' :
                                pontos_X += 1
                            
                            if matriz[n][c] == 2 and jogo[c] == '0' :
                                pontos_0 += 1
                        else:break
                    else:break
            else:break
        else:break
    if pontos_0 == 3:
        return 2
    elif pontos_X == 3:
        return 1


jogo = ['1','2','3','4','5','6','7','8','9']#jogo imaginario



vitorias = gerar_vitorias('vitorias')   
x = consultar_vitoria(vitorias,jogo)
casas = [0,1,2,3,4,5,6,7,8]

icone = str(input('escolha qual voce quer usar [0/X]: ')).upper()
if icone == 'X':
    icone_bot = '0'
if icone == '0':
    icone_bot = 'X'



for n in range(0,5):
    os.system('cls')
    print(f'''            [{jogo[0]}] [{jogo[1]}] [{jogo[2]}]
            [{jogo[3]}] [{jogo[4]}] [{jogo[5]}]
            [{jogo[6]}] [{jogo[7]}] [{jogo[8]}]''')
    escolha = int(input('digite qual lugar voce quer escolher: '))
    jogo[escolha-1] = str(icone)
    casas.remove(int(escolha)-1)
    if len(casas) > 0:
        escolha_bot = choice(casas)
        jogo[escolha_bot] = str(icone_bot)
        casas.remove(escolha_bot)
    x = consultar_vitoria(vitorias,jogo)
    if x == 1:
        os.system('cls')
        print(f'''            [{jogo[0]}] [{jogo[1]}] [{jogo[2]}]
            [{jogo[3]}] [{jogo[4]}] [{jogo[5]}]
            [{jogo[6]}] [{jogo[7]}] [{jogo[8]}]''')
        print('X ganhou')
        break
    if x == 2:
        os.system('cls')
        print(f'''            [{jogo[0]}] [{jogo[1]}] [{jogo[2]}]
            [{jogo[3]}] [{jogo[4]}] [{jogo[5]}]
            [{jogo[6]}] [{jogo[7]}] [{jogo[8]}]''')
        print('bola ganhou')
        break


