# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

# – Média abaixo de 5.0: REPROVADO

# – Média entre 5.0 e 6.9: RECUPERAÇÃO

# – Média 7.0 ou superior: APROVADO

n1 = float(input('Digite a primeira nota: '))

n2 = float(input('\nDigite a segunda nota: '))

soma = n1 + n2
media = soma / 2

print(f'\nSua primeira nota foi {n1} e a segunda nota foi {n2}, a soma de ambas as notas é de {soma} e sua média é de {media:.2f}!\n')

if media < 5.0:
    print('Sua média foi inferior a 5.0! REPROVADO')
elif media > 5.0 and media < 6.9: 
    print('Sua média está entre 5.0 e 6.9! RECUPERAÇÃO')
else:
    print('Sua média é superior a 7.0! APROVADO')
