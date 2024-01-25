# 1 - FAZER UM ALGORITMO QUE AO RECEBER O SALÁRIO DE UM FUNC, CALCULE O VALOR DO NOVO SALÁRIO REAJUSTADO DE ACORDO COM A TABELA ABAIXO:

# SALÁRIO ATUAL - REAJUSTE
# ABAIXO DE R$ 500,00 - 15%
# DE R$ 500,00 ATÉ R$ 1.000,00 - 10%
# ACIMA DE R$ 1.000,00 - 5 %



salario = float(input("Digite o valor do seu salário: "))

if salario < 500.00:
    porcentagem = (salario *0.15)
    reajuste = (salario + porcentagem)

elif salario >= 500.00 or salario <= 1000.00:
    porcentagem = (salario * 0.10)
    reajuste = (salario + porcentagem)

elif salario > 1000.00:
     porcentagem = (salario * 0.05)
     reajuste = (salario + porcentagem)


print("Seu reajuste foi de RS {} e a soma do reajuste mais o salário é de R$ {}" .format(porcentagem, reajuste))