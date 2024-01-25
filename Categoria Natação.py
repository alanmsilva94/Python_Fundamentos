# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER



from datetime import date

ano_nasc = int(input('Informe seu ano de nascimento: '))

ano_atual = date.today().year

idade = abs(ano_atual - ano_nasc)

print(f'\nVocê nasceu em {ano_nasc} e estamos no ano de {ano_atual}, então você tem {idade} anos!\n')

if idade <= 9:
    print('Você é da categoria MIRIM!')
elif idade <= 14:
    print('Você é da categoria INFANTIL!')
elif idade <= 19:
    print('Você é da categoria JÚNIOR!')
elif idade <= 25:
    print('Você é da categoria SÊNIOR!')
else:
    print('Você é da categoria MASTER!')
