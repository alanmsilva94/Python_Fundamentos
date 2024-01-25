# Comando para atribuir uma variável com input
num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
soma = num1 + num2
subtracao = num1 - num2
divisao = num1 / num2
multiplicacao = num1 * num2
print('A soma entre {} e {} é igual {}'.format(num1, num2, soma))
print('A subtração entre {} e {} é igual {}'.format(num1, num2, subtracao))
print('A divisão entre {} e {} é igual {}'.format(num1, num2, divisao))
print('A multiplicação entre {} e {} é igual {}'.format(num1, num2, multiplicacao))