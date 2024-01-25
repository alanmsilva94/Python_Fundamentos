# FAÇA UM ALGORITMO EM LIGAGUEM PYTHON QUE RECEBA DUAS NOTAS E CALCULE A MÉDIA E MOSTRE O RESULTADO
# CASO A MÉDIA SEJA IGUAL OU SUPERIOR A 7, APRESENTAR A MESANGEM "APROVADO", CASO CONTRÁRIO, "REPROVADO".


def soma (n1, n2, n3, n4):
    return (n1 + n2 + n3 + n4)

def media (n1, n2, n3, n4):
    return (n1 + n2 + n3 + n4) / 4

n1 = float(input("Digite a primeria nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

resultado = media (n1, n2, n3, n4)

while n1 > 10 or n1 < 0:
     n1 = float(input("N1 está com valor inválido, digite novamente: "))

while n2 >10 or n2 < 0:
    n2 = float(input("N2 está com valor inválido, digite novamente: "))
    
while n3 > 10 or n3 < 0: 
    n3 = float(input("N3 está com valor inválido, digite novamente: "))

while n4 > 10 or n4 <0:
    n4 = float(input("N4 está com valor inválido, digite novamente: "))

print("A soma das notas: {} + {} + {} + {} = {}. A média é: {}" .format(n1, n2, n3, n4, soma(n1, n2, n3, n4), media (n1, n2, n3, n4)))

if resultado > 5:
    print("APROVADO")
else:
    print("REPROVADO")





