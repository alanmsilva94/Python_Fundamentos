'''Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''



flag = "S"
c = 0
soma = 0
maior = 0
menor = 0



while flag in 'Ss':
    num = int(input('Digite um número: '))
    c += 1
    soma += num
    if c == 1:
        maior = menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    flag = str(input('Digite S para continuar e N para encerrar: '))
print(f'A média entre todo os valores é de {soma / c:.2f} e o maior número é {maior} e o menor é {menor}')