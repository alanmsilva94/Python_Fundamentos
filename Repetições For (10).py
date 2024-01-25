# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.


idade_grupo = 0
m_velho = 0
nome_velho = ''
fem_abaixo_vinte = 0

for c in range (1, 5):
    print('--------- {c}ª PESSOA ---------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    idade_grupo += idade
    

    if c == 1 and sexo in 'Mm':
        m_velho = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > m_velho:
        m_velho = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        fem_abaixo_vinte += 1

    media = idade_grupo / c

print(f'A média de idade do grupo é de {media}.')
print(f'O homem mais velho do grupo tem {m_velho} anos e se chama {nome_velho}.')

if fem_abaixo_vinte > 0:
    print(f'Ao todo são {fem_abaixo_vinte} mulheres abaixo de 20 anos.')
else:
    print(f'No grupo não tem nenhuma mulher abaixo de 20 anos.')