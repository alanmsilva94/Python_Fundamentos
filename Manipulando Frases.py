# fatiando uma string 

frase = 'Curso em Video Python'

'''print(frase[0:5])
print(frase[0:15])
print(frase[15:])
print(frase[:10])
print(frase[:])
print(frase[9::3])'''


# Analisando uma string

''' Len conta quantos caracteres tem na frase contando os espaços'''
print(len(frase))

'''Conta quantas vezes aparece a letra "o" minuscula, python é case sensitive, ou seja, ele identifica o que é maiuscula ou minuscula'''   
print(frase.count('o'))

'''Verifica quantas vezes ele encontrou uma determinada letra ou palavra, informando seu ponto de inicio'''
print(frase.find('deo'))
print(frase.find('Android'))


# Verificando se existe a palavra 'curso' dentro da variavel 'frase' utilizando o operador in, isso ira retorno True ou False
print('Curso' in frase)



# Transformando uma string

'Função replace troca uma palavra por outra'
print(frase.replace("Python", "Android"))

'Upper deixa todas letras em maisculas'
print(frase.upper())

'Lower deixa todas letras em minusculo'
print(frase.lower())

'Capitalize deixa apenas a primeira letra do texto em maiuscula, as demais ficam minusculas'
print(frase.capitalize())

'Title faz com que as letras entre um intervalo de cada espaço fique maiuscula'
print(frase.title())


frase1 = "   Aprenda Python   "
print(frase1)

'Strip remove os espaços desnecessário no começo e no final'
print(frase1.strip())
print(frase1.rstrip())
print(frase1.lstrip())

# Dividindo de string

print(frase.split())

# Junção de string

print('-'.join(frase))


'''nome = str(input('Digite o seu nome completo: ')).strip()

print('\nAnalisando seu nome!\n')

print('Seu nome em maiscúlucas é', nome.upper())
print('Seu nome em minúsculas é', nome.lower())
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
print(f'Seu primeiro nome é {nome[0:4]} e ele tem {len(nome[0:4])} letras.')'''

# Separando dígitos de um número

num = int(input('Informe um número: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10


print(f'Analisando o número: {num}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')

# Verificando texto

cid = str(input('Digite a cidade que você nasceu: ')).strip()
print(cid[0:5].upper == "Santo")