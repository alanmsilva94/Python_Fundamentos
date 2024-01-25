nota1= int(input("Digite a primeira nota : "))
nota2= int(input("Digite a segunda nota : "))
nota3= int(input("Digite a terceira nota : "))

nome = 'Rafael'

media = (nota1 + nota2+ nota3) / 3

print("Aqui é o tipo: " , type(len(nome)))

if media < 6 :
    print("Você foi reprovado.")
    print("A sua média foi : {:.2f}" .format(media))
    print("A média entre nota 1 {:.2f} e nota 2 {:.2f} e nota 3 {:.2f} foi : {:.2f}" .format(nota1,nota2, nota3,media))

else:
        print("Você foi aprovado.")
        print("A sua média foi : {:.2f}" .format(media))
        print("A média entre nota 1 {:.2f} e nota 2 {:.2f} e nota 3 {:.2f} foi : {:.2f}" .format( nota1,nota2, nota3,media))