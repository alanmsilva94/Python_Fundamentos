# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint

print('''Escolha uma das opções abaixo:
[0] - Pedra
[1] - Papel
[2] - Tesoura''')

opcoes = ('Pedra', 'Papel', 'Tesoura')

jogador = int(input('Qual é a sua jogada: '))
computador = randint(0,2)


if (jogador == 3 or jogador > 3):
    print('Você não escolheu um item correto!!!')
else:
    print(f'Você escolheu: {opcoes[jogador]}')    
    print(f'O Computador escolheu: {opcoes[computador]}')
    tabela = ((0, 1, 2), (2, 0, 1), (1, 2, 0))
    jogada = tabela[computador][jogador]

    if jogada == 0:
        resultado = 'Deu empate vocês escolhera a mesma peça'
    elif jogada == 1:
        resultado = 'Você ganhou!'
    else:
        resultado = 'O computador ganhou!'

    print(resultado)


