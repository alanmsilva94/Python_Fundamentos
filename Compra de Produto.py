# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço normal 
# – 3x ou mais no cartão: 20% de juros


produto = float(input('Digite o valor do produto: R$ '))

print('''Escolha umas das formas de pagamento abaixo:\n
[1] - à vista dinheiro/cheque: 10% de desconto\n
[2] - à vista no cartão: 5% de desconto\n
[3] - em até 2x no cartão: preço normal\n
[4] – 3x ou mais no cartão: 20% de juros\n''')




condição_pgto = int(input('\nEscolha a forma de pagamento: '))

if condição_pgto == 1:
    print(f'O produto custa R$ {produto:.2f} com desconto de 10% que é R$ {produto * 0.10:.2f}, o valor total ficará R$ {produto - (produto * 0.10):.2f}!')
elif condição_pgto == 2:
    print(f'O produto custa R$ {produto:.2f} com desconto de 5% que é R$ {produto * 0.05:.2f}, o valor total ficará R$ {produto - (produto * 0.05):.2f}!')
elif condição_pgto == 3:
    print(f'O produto custa R$ {produto:.2f}, divido em 2x ficará duas parcelas de R$ {produto / 2:.2f} SEM JUROS!')
elif condição_pgto == 4:
    total = produto + (produto * 0.20)
    totalparcel = int(input('\nDigite a quantidade de parcelas: '))
    parcelas = total / totalparcel
    print(f'\nSua compra será divida em {totalparcel}x de R$ {parcelas:.2f} COM JUROS!')
else:
    print('Opção de pagamento inválida!')
