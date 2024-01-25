'''
dia = int(input("Digite úm número: "))

if dia == 1:
    print('Domingo')
elif dia == 2: 
    print("Segunda")
elif dia == 3:
    print("Terça")
elif dia == 4:
    print('Quarta')
elif dia == 5:
    print('Quinta')
elif dia == 6:
    print('Sexta')
elif dia == 7:
    print('Sabádo')
else:
    print("Dia inválido")

'''    


'''
dia = int(input("Digite úm número: "))

match dia:

    case 1: 
        print('Domingo')
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print('Quarta')
    case 5:
        print("Quinta")
    case 6:
        print('Sexta')     
    case 7:
        print('Sabádo')
    case _:
        print("Data inválida")
'''

'''

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))


print("Digite + para adição")
print("Digite - para subtração")
print("Digite * para multiplicação")
print("Digite / para divisão")



operacao = input('Digite a operação desejada: ')

match operacao:
    
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        print(num1 / num2)
    case _:
        print("Operação inválida")
'''

# Dado o valor do produto e a forma de pagamente

# 1 - à vista
# 2 - à prazo
# Se o produto for pago à vista aplique um desconto de !0% antes de mostrar o valor finaç, senão informe o mesmo valor do produto

valor = float(input('Digite o preço do produto: R$ '))

print("Digite 1 para pagamento à vista")
print("Digite 2 para pagamento à prazo")

pgto = input("Digite a forma de pagamento: ")

match pgto:
    case '1':
        desconto = valor * 0.10
        valor_desconto = valor - desconto
        print("Valor à vista com desconto de R$ {:.2f} é de R$ {:.2f}" .format(desconto, valor_desconto))
    case '2':
        print("Pagamento à prazo")
    case _:
        print('Escolha uma forma de pagamento')    