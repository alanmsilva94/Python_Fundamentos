
Nome = input("informe o seu nome: ")


print("Quantidade de caracteres",len(Nome))
print("Quantidade de caracteres", Nome.upper())
print("Quantidade de caracteres", Nome.lower())
print("Quantidade de caracteres", Nome.capitalize())
print('Alterar Caracteres', Nome.replace('a', '1'))
print('Alterar Caracteres', Nome.replace('A', '1'))
print('Nome sem espaços: ', Nome.replace(' ', ''))

print('Alterar Caracteres', Nome.replace('A', '1').replace('a', '2'))
print('Alterar Caracteres', Nome.upper().replace('A', '1'))

n1 = Nome.replace('A', '1')
print('Alterar Caracteres', n1.replace('a', '2'))



espaco = Nome.find(' ')
print('Somenete o primeiro nome: ', Nome.capitalize().replace('A', '2')[0:espaco])


