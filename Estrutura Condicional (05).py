letra= input("Digite Uma Letra : ")

letra=letra.lower()

if letra == "a":
    print("É uma vogal")
elif letra == "e":
    print("É uma vogal")
elif letra == "i":
    print("É uma vogal")
elif letra == "o":
    print("É uma vogal")
elif letra == "u":
    print("É uma vogal")
elif letra.isnumeric():
    print("Digite uma letra")
else:
    print("É uma Consoante")    
