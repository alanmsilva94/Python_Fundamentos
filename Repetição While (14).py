# Faça um programa em Python que imprima os 10 primeiros números naturais.

'''
c = 0

while c < 11: 
    print(c)
    c = c + 1
'''


''''
Faça um programa que solicite a senha de um usuário e depois, peça para digitar novamente até que as duas senhas seja correspondentes. 
Exibir a mensagem: Senha errada, digite novamente.
'''


'''
senha1 = str(input("Digite a primeira senha: ")).upper()
senha2 = str(input("Digite a segunda senha: ")).upper()

while senha1 != senha2:
    print("Senhas erradas, digite novamente!")
    senha1 = str(input("Digite senha novamente: "))
    senha2 = str(input("Digite senha novamente: "))
print("Senhas confirmada!")
'''

#Faça um programa em Python que leia n números inteiros a partir do teclado, até que o usuário digite 0. Ao final, mostre a soma de todos os números.

'''
soma = 0
num1 = int(input("Digite um número: "))

while num1 != 0:
    soma += num1
    num1 = int(input("Digite um número (zero para parar): "))
print("A soma para todos os numeros é: {}" .format(soma))

'''

#Faça um programa em Python que leia n números inteiros a partir do teclado, até que o usuário digite 0. Ao final, mostre informe o maior número digitado.

'''
maior = -1
num1 = int(input("Digite um número: "))

while num1 >= 0:
    if num1 > maior:
        maior = num1
    num1 = int(input("Digite um número (-1 para parar): "))
print("O maior número é: {}" .format(maior))

'''


#Faça um programa em Python que leia n números inteiros a partir do teclado, até que o usuário digite 0. Ao final, mostre informe o menor número digitado.

maior = 0
menor = 0
num1 = int(input("Digite um número: "))

while num1 > 0:
    if (num1 > maior):
        maior = num1
    elif (num1 < menor or menor == 0):    
        menor = num1    
    num1 = int(input("Digite um número ou zero para encerrar a execução: "))    
print("O menor nº {}" .format(menor))
print("O maior nº {}" .format(maior))