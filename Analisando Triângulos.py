# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes


r1 = float(input('Primeiro segmento: '))
r2 = float(input('\nSegundo segmento: '))
r3 = float(input('\nTerceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\nOs segmentos podem criar um triângulo!\n')
    if r1 == r2 and r1 == r3 and r2 == r3:
        print('EQUILÁTERO: todos os lados iguais')
    elif r1 == r2 and r1 == r3 and r2 != r3:
        print('ISÓSCELES: dois lados iguais, um diferente')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('ESCALENO: todos os lados diferentes')

else:
    print('Os segmentos não podem criar um triângulo!\n')
