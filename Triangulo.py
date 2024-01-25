# Faça um programa que leia um comprimento de três retas e diga ao usuário se elas podem ou não criar um triângulo


r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem criar um triângulo!')
else:
    print('Os segmentos não podem criar um triângulo!')





