'''
    Crie um jogo de pedra, papel ou tesoura. Você deverá jogar contra o computador e escolher sempre uma das opções: 
    
    1 - Pedra
    2 - Papel
    3 - Tesoura

    O computador deve sempre sortear um número de 1 a 3 para jogar também.
    Armazene todos os resultados em uma lista e, no final, apresente o vencedor.
    Encerre o jogo ao digita 0.
'''

from random import randint

print('Bem-vindo ao Jokenpô!')
print('Digite o número de uma das opções a seguir ou 0 (zero) para sair. \n')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura \n')

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while x < min or x > max:
        x = int(input(pergunta))
    return x

def vencedor(jogador, cpu):
    global jogadas, vit_jogador, vit_cpu, empates # trazemos as variáveis globais pra dentro da função

    if jogador == 1: # Pedra
        print('Jogador: PEDRA')
        if cpu == 1: # Pedra
            print('Computador: PEDRA')
            empates += 1
            print('Empate na jogada!')
        elif cpu == 2: # Papel
            print('Computador: PAPEL')
            vit_cpu += 1
            print('O Computador ganhou!')
        elif cpu == 3: # Tesoura
            print('Computador: TESOURA')
            vit_jogador += 1
            print('Você ganhou!')
    elif jogador == 2: # Papel
        print('Jogador: PAPEL')
        if cpu == 1: # Pedra
            print('Computador: PEDRA')
            vit_jogador += 1
            print('Você ganhou!')
        elif cpu == 2: # Papel
            print('Computador: PAPEL')
            empates += 1
            print('Empate na jogada!')
        elif cpu == 3: # Tesoura
            print('Computador: TESOURA')
            vit_cpu += 1
            print('O Computador ganhou!')
    elif jogador == 3: # Tesoura
        print('Jogador: TESOURA')
        if cpu == 1: # Pedra
            print('Computador: PEDRA')
            vit_cpu += 1
            print('O Computador ganhou!')
        elif cpu == 2: # Papel
            print('Computador: PAPEL')
            vit_jogador += 1
            print('Você ganhou!')
        elif cpu == 3: # Tesoura
            print('Computador: TESOURA')
            empates += 1
            print('Empate na jogada!')
    print()
    _resultados = [vit_jogador, vit_cpu, empates] # MOSTRAR AS VITÓRIAS
    return _resultados

resultados = []

vit_jogador = 0
vit_cpu = 0
empates = 0

while True:
    jogador = valida_int('Escolha sua jogada: ', 0, 3)
    print()
    if not jogador: # == 0
        print('Jogo Encerrado.')
        break
    cpu = randint(1, 3)
    resultados = vencedor(jogador, cpu)
    #print(jogadas)
    print('Placar => Você: {}, Computador: {}, Empates: {} \n' .format(resultados[0], resultados[1], resultados[2]))

if resultados[0] > resultados[1]:
    print('Parabéns! Você venceu o jogo!')
else:
    print('Não foi dessa vez. O Computador venceu o jogo!')