# Escreva um programa que faça o PC "pensar" em um número int de 0 a 5 e peça para o usuário tentar descobrir qual número escolhido pelo PC
# O programa deverá escrever se você venceu ou perdeu

import random
from time import sleep  

computador =  random.randint(0,5)

print('-=-' * 30)
print('Vamos jogar um jogo de advinhação! Vou pensar em um número do  0 a 5. Tente Adivinhar...')
print('-=-' * 30)

jogador = int(input('\nDigite um número de 0 a 5: '))

print('\nPROCESSANDO...')
sleep(3)

print(f'\nVocê escolheu {jogador} o computador escolheu {computador}!\n')

if jogador == computador:
    print('Parabéns você acertou!')
else:
    print('Você errou, mais sorte na próxima!')
