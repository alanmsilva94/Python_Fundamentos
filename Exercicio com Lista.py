nota1= int(input("Digite a primeira nota : "))
nota2= int(input("Digite a segunda nota : "))
nota3= int(input("Digite a terceira nota : "))
resultado = [nota1, nota2, nota3]

resultado.sort()
valor1=(sorted(resultado)[-2])
resultado = valor1
print("{}" .format(resultado))