# Exercício Python 50: Desenvolva um programa que leia seis números inteiros e 
# mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.





soma = 0
cont = 0

for c in range(1, 7):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'Você inseriu um total de {cont} número e a soma somente dos números pares é de {soma}!')

  

   
   