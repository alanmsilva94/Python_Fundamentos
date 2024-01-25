# Faça um programa que receba a velocidade do carro. Se passar de 80km/h, mostrar uma mensagem dizendo que foi multado.
# A multa vai custar R$ 7,00 por cada KM acima do limite 

velocidade = float(input('Qual a velocidade atual do carro? '))

if velocidade > 80:
    print(f'\nVelocidade acima do permitido de 80km/h!\n\nVoce foi multado em R$ {(velocidade - 80.00) * 7.00:.2f}!')
else:
    print('Velocidade dentro do permitido tenha uma boa viagem!')




# Desenvolva um programa que pergunte a distancia de uma viagem  em KM. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens até 200km
# e R$ 0,45 para viagens acima de 200km.

distancia = float(input('\nQual a distancia da sua viagem? '))

print(f'Você está preste a começar uma viagem de {distancia:.2f}km. ')

if distancia <= 200:
    print(f'O preço da sua viagem é de R$ {distancia * 0.50:.2f}.')
else:
    print(f'O preço da sua viagem é de R$ {distancia * 0.45:.2f}.')    

