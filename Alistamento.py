# Faça um programa que leia o ano de nascimento de um jovem e informe, 
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.



from datetime import date

ano_de_nasc = int(input('Digite seu ano de nascimento: '))

ano_atual = date.today().year

idade = abs(ano_de_nasc - ano_atual)

print(f'Quem nasceu em {ano_de_nasc} tem {idade} anos em {ano_atual}!')




if idade == 18:
    print(f'Você tem que se alistar imediatamente!!!')

elif idade > 18:
    saldo = abs(18 - idade)
    print(f'Você já deveria ter se alistado a há {abs(saldo)} anos!')
    ano = abs(ano_atual - saldo)
    print(f'Seu alistamento foi em {abs(ano)}')

elif idade < 18:
    saldo = abs(idade - 18)
    print(f'Ainda faltam {abs(saldo)} anos para o alistamento!') 
    ano = abs(ano_atual + saldo)
    print(f'Seu alistamento será em {abs(ano)}!')

