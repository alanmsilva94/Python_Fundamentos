# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

n = 0
c = 0
soma = 0

while True:
    n = int(input('Digite um número ou [999] para encerrar: '))
    if n == 999:
        break
    c = c + 1
    soma = soma + n
print(f'Foi digitado um total de {c} número e a soma de cada número digitado é de {soma}')

