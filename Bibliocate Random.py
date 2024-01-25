#Exeercicio bibloteca random

import random

# para importar uma única função da biblioteca deve-se usar FROM "BIBLIOTECA" IMPORT "FUNÇÃO DA BIBLIOCATE" ex: from random import choice

# Um professor quer sortear um dos seus  quatros alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do  escolhido.

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

lista = [n1, n2, n3, n4]
'''escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')'''

# Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada dos nomes.abs

random.shuffle(lista)
print('A ordem de apresentação será!')
print(lista)