# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

# A) qual é o total gasto na compra.

# B) quantos produtos custam mais de R$1000.

# C) qual é o nome do produto mais barato.

total_gasto = 0
produtos_mil = 0
cont = 0
menor = 0
produto_barato = ' '


while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$ '))
    total_gasto = total_gasto + preco
    cont = cont + 1

    if preco > 1000:
        produtos_mil = produtos_mil + 1
    if cont == 1 or preco < menor:
        menor == preco
        produto_barato = nome
    opcao = ' ' 
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar Sim ou Não [S/N]: ')).upper().strip()[0]
    if opcao == 'N':
        print('{:-^40}'.format('\nCompra Concluída\n'))
        break

print(f'O total gasto em compras foi de R$ {total_gasto:.2f}!')
print(f'Na compra efetuada existe {produtos_mil} que custam acima de mil reais!')
print(f'O produto mais barato foi a(o) {produto_barato} que custa R$ {menor}!')

barato = {nome:preco}
print (barato)