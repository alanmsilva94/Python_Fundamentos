# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos.

# B) quantos homens foram cadastrados.

# C) quantas mulheres tem menos de 20 anos.


tot18 = totH = totM20 = 0


while True:
    idade = int(input('Informe a sua idade: '))
    sexo = str(input('Informe seu sexo Masculinho/Feminino [M/F]: ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Dados inválidos, por favor informe seu sexo [M/F]: ')).upper().strip()[0]



    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == "F" and idade < 20:
        totM20 += 1


    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar Sim ou Não [S/N]: ')).upper().strip()[0]
    if opcao == 'S':
        print('Cadastre uma nova pessoa!')
    elif opcao == 'N':
        break
        print('Cadastro encerrado.')
print(f'Total de pessoas cadastradas acima de 18 anos: {tot18}.')
print(f'Total de homens cadastrados: {totH}.')
print(f'Total de mulheres com menos de 20 anos cadastradas: {totM20}.')