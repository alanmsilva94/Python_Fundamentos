
# def = Estou definindo uma função

def soma(x, y):
    print('Soma: ', x+y)
def subtracao(x, y):
    print('Subtração: ', x-y)
def multiplicacao(x, y):
    print('Multiplicação: ', x*y)
def divisao(x, y):
    print('Divisão: ', x/y)


opcao = 1

while opcao:
    x = float(input('Digite seu primeiro número: '))
    y = float(input('Digite seu segundo número: '))

    print("1. Somar")
    print("2. Subutrair")
    print("3. Multiplicar")
    print("4. Dividir")

    operador = int(input('Opção: '))

    if operador == 1:
        soma(x,y)
    elif operador == 2:
        subtracao(x,y)
    elif operador == 3:
        multiplicacao(x,y)
    elif operador == 4:
        divisao(x,y)


    opcao = input("Aperte 0 para Continuar ou Enter para Sair: ")

    if opcao == 0:
        opcao =int(opcao)
print("Até logo!")





# Utilizando Match

def soma(x, y):
    print('Soma: ', x+y)
def subtracao(x, y):
    print('Subtração: ', x-y)
def multiplicacao(x, y):
    print('Multiplicação: ', x*y)
def divisao(x, y):
    print('Divisão: ', x/y)


opcao = 1

while opcao:
    try:
        x = float(input('Digite seu primeiro número: '))
    except:
        print("Valor inserido não é númerico, digite um número!")
        x = float(input('Digite novamente o primeiro número: '))
       
    y = float(input('Digite seu segundo número: '))

    print("1. Somar")
    print("2. Subutrair")
    print("3. Multiplicar")
    print("4. Dividir")

    operador = int(input('Opção: '))

    match operador:
        case 1:
            soma(x,y)
        case 2:
            subtracao(x,y)
        case 3:
            divisao(x,y)
        case 4:
            multiplicacao(x,y)


    opcao = input("Aperte 0 para Sair ou Enter para continuar: ")

    if opcao == 0:
        opcao =int(opcao)




