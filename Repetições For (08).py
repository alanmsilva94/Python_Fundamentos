# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date  

ano_atual = date.today().year

maior = 0
menor = 0

for c in range (1, 7 + 1):
    ano_nasc = int(input(f'Em que anos a {c} pessoa nasceu: '))
    maioridade = ano_atual - ano_nasc
    if maioridade >= 18:
        maior += 1
    else:
        menor += 1

print(f"\nAo todo tivemos {maior} pessoas maiores de idade.")
print(f'\nE também tivemos {menor} pessoas menores de idade.')