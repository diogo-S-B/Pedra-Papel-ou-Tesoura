from random import choice
from time import sleep

lista = ['pedra', 'papel', 'tesoura']


def lobby():
    msg = 'Bem vindo ao Pedra, Papel ou Tesoura'
    new_msg = len(msg) + 4
    print('='*new_msg)
    print(f'  {msg}')
    print('='*new_msg)


def condicoes(ask, chip):
    # Chip Vencedor:
    if ask == chip:
        print('empate')
        print(f'O chip escolheu: {chip}')
        
    elif ask == 'pedra' and chip == 'papel':
        print('O chip é o vencedor')
        print(f'O chip escolheu: {chip}')
        return True

    elif ask == 'papel' and chip =='tesoura':
        print('O chip é o vencedor')
        print(f'O chip escolheu: {chip}')
        return True

    elif ask == 'tesoura' and chip == 'pedra':
        print('O chip é o vencedor')
        print(f'O chip escolheu: {chip}')
        return True

    #Jogador ganha

    elif ask == 'pedra' and chip == 'tesoura':
        print(f'Você é o vencedor')
        print(f'O chip escolheu: {chip}')
        return False
    elif ask == 'papel' and chip == 'pedra':
        print('Você é o vencedor')
        print(f'O chip escolheu: {chip}')
        return False
    else:
        if ask == 'tesoura' and chip == 'papel':
            print('Você é o vencedor')
            print(f'O chip escolhou: {chip}')
            return False


tentativas = 0
chip_win = 0
jogador_win = 0
while True:
    tentativas +=1
    escolha = choice(lista)
    lobby()
    ask1 = str(input('Escolha: '))
    resp = condicoes(ask1, chip=escolha)
    if resp == True:
        chip_win += 1
    elif resp == False:
        jogador_win += 1

    kog = str(input('Deseja jogar novamente? \n: ')).lower().strip()
    if kog not in 'sim':
        break


print(f'De {tentativas} tentativas o chip ganhou {chip_win} e voce ganhou {jogador_win}')