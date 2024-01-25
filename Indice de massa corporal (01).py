# *** CALCULADORA DE IMC ***

peso = float(input('Digite seu peso: '))
altura = float(input('Difite sua altura: '))

imc = peso / altura ** 2
print('Seu imc é: {}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 24.9:
    print('Peso normal')
elif imc < 29.9:
    print('Sobrepeso')       
elif imc < 34.9:
    print('Obesidade Grau I')
elif imc < 39.9:
    print('Obesidade Grau II')
else:
    print('Obesidade Grau III ou Mòrbida')