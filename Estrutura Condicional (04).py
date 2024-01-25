Letra= input ("Digite uma letra : ")
Letra = Letra.lower()
if Letra in ("a","e", "i", "o", "u"):
    print("Vogal")
elif Letra.isnumeric():
    print("Digite uma letra")
else:
    print("Consoante")