# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o "valor da casa", o "salário" do comprador e em "quantos anos" ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negaado.

salario = float(input('Digite seu salário: R$ '))
valor_da_casa = float(input('Digite o valor da casa: R$ '))
qtd_parcelas = int(input('Digite a quantidade de meses do financiamento: '))
anos = qtd_parcelas / 12

prestacao_mensal = valor_da_casa / qtd_parcelas
consigo_pagar = salario * 0.30

print(f'Para pagar uma casa de R$ {valor_da_casa:.2f} em {anos:.0f} anos, a prestação será de R$ {prestacao_mensal:.2f}!')

if consigo_pagar >= prestacao_mensal:
    print('Empréstimo liberado!')
elif consigo_pagar < prestacao_mensal:
    print('Empréstimo negado!')

