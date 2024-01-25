# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.


from random import randint
from time import sleep


print('''Sou seu computador...
Acabei de pensar é um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')

computador = randint(0, 10)
jogador = int(input('Esolha um número entre 0 e 10: '))
palpites = 0


while jogador != computador:
    palpites = palpites + 1
    if jogador < computador:
        print("Número menor do que o do computador.")
        jogador = int(input('Tente novamente: '))
    elif jogador > computador:
        print('Número maior do que o do computador.')
        jogador = int(input('Tente novamente: '))

print(f'\nVocê escolheu {jogador} o computador escolheu {computador}!')
sleep(2)
print(f'Foram necessário {palpites} tentativas para acerta.')

