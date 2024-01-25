'Criar uma tabuada'

multiplicador = int(input("Informe o multiplicador: "))

for i in range(1, 11):
    print("{} * {} = {}".format(multiplicador, i, i*multiplicador))


for i in range(1, 11):
     print('{: >4} {: >4} {: >4} {: >4} {: >4} {: >4} {: >4} {: >4} {: >4} {: >4}'.format(i, i*2, i*3, i*4, i*5, i*6, i*7, i*8, i*9, i*10))



