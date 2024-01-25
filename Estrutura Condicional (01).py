nota1= int(input("Digite a primeira nota : "))
nota2= int(input("Digite a segunda nota : "))
nota3= int(input("Digite a terceira nota : "))

if nota1> nota2:
    if nota1 < nota3:
        mediana= nota1       
    elif nota2 > nota3:
        mediana = nota2
    else:
        mediana = 3
else:
    if nota1 > nota2 :
        mediana = nota1
    elif nota2 < nota3:
        mediana = nota2
    else:
        mediana = nota3
print("Mediana = {}" .format(mediana))


