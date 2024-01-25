# Criando um jogo de Jokenpô

import random

print('\nEscolha uma das opções abaixo para jogar:\n')

print('[0] Pedra')
print('[1] Papel')
print('[2] Tesoura\n')


opcao = 's'

while opcao.upper() == 'S':
    computador = random.randint(0,2)
    jogador = int(input('Esolha uma opcao para se jogar: '))

    pecas = ('Pedra', 'Papel', 'Tesoura')

    if (jogador == 3 or jogador > 3):
        print('Você não escolheu um item correto!!!')
    else:
        print(f'Você escolheu: {pecas[jogador]}')    
        print(f'O Computador escolheu: {pecas[computador]}')
        tabela = ((0, 1, -1), (-1, 0, 1), (1, -1, 0))
        jogada = tabela[computador][jogador]

        if jogada == 0:
            resultado = 'Deu empate vocês escolhera a mesma peça'
        elif jogada == 1:
            resultado = 'Você ganhou!'
        else:
            resultado = 'O computador ganhou!'

        print(resultado)
    opcao = input('Jogar novamente? Aperte S(sim) para jogar novamente. ')    



