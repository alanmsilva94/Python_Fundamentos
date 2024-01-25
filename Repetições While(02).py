# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

# [ 1 ] somar

# [ 2 ] multiplicar

# [ 3 ] maior

# [ 4 ] novos números

# [ 5 ] sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso.


num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
operacao = 0

while operacao != 5:
    print('''   
    [1] - Somar
    [2] - Multiplicar
    [3] - Maior número
    [4] - Novos números
    [5] - Sair do programa\n''')
    operacao = int(input('Escolha a operação desejada: '))
    if operacao == 1:
        soma = num1 + num2
        print(f'{num1} + {num2} = {soma}')
    elif operacao == 2:
        multiplicar = num1 * num2
        print(f'{num1} * {num2} = {multiplicar}')
    elif operacao == 3:
        if num1 > num2:
            maior = num1
        elif num2 > num1:
            maior = num2
        print(f'Entre {num1} e {num2} o maior número é {maior}')
    elif operacao == 4:
        print('Informe os números novamente.')
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
    elif operacao == 5:
        print('Encerramos por hoje!')
    else:
        print('Opção inválida. Tente novamente.')

