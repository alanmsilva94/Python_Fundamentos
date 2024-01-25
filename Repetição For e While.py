'Faça um programa que mostre os números pares que estão entre 1 e 50'
"Faca um programa que recebe 6 números inteiros e mostra a soma apenas dos números pares."
'Faça um programa que leia um numero inteiro e diga se ele é ou não um número primo'



for i in range(1,51):
    if i % 2 == 0:
        print(i)


resultado = 0

for i in range(1,7):
    numero = int(input('Digite o {}º valor: ' .format(i)))
    if numero % 2 == 0:
        resultado += numero
print("A soma dos números pares é: {}".format(resultado))



num = int(input('Digite o valor: '))
multi = 0

for i in range(2,num):
    if num % i == 0:
        print("Multiplo de", i)
        multi += 1
if multi == 0:
    print('É primo')
else:
    print('Não é primo')           


'''''''''''''''''''''''''''''''''''''Estrutora de repetição WHILE''''''''''''''''''''''''''''''''

contador = 0

while contador < 10: 
    print("Olá")
    contador = contador + 1


# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado peça a digitação novamente
sexo = str(input("Digite seu sexo: ")).upper()

while sexo not in "MF":
    sexo = str(input("Dados inválidos, por favor informe seu sexo:"))
print("Sexo {} registado com sucesso" .format(sexo))



# Faça um programa que receba um número e mostre o seu fatorial
num = int(input('Digite um número: '))
c = num
f = 1 
print("Calculando fatorial de {}".format(num))
while c > 0:
    print('{}'.format(c))
    print('x' if c > 1 else ' = ')
    f *= c
    c -= 1
print('{}'.format(f))    


