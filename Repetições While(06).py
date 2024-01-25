'''Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

num = 0
c = 0
soma = 0
flag = 999
num = int(input('Digite um número [Digite 999 para encerrar]: '))

while num != flag:
    c += 1
    soma += num
    num = int(input('Digite um número [Digite 999 para encerrar]: '))
print(f'Foram digitados {c} e a soma deles foi de {soma}')
print('fim')

