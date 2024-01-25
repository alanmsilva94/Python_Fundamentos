#importar biblioteca com funções estatistica

'''
import statistics
print(statistics.mean([1,2,3,4,5])) #calcula a média
print(statistics.median([1,2,3,4,5,6,7,8,9])) #calcula a mediana
print(statistics.median_high([1,2,3,4,5,6,7,8,9])) #calcula a mediana superior
print(statistics.median_low([1,2,3,4,5,6,7,8,9])) #calcula a mediana inferior
'''

# Site com todas a bibliotecas do Python

'''
https://docs.python.org/pt-br/3/library/index.html
'''


#importar biblioteca com funções de datas

from datetime import datetime
'''
atual = datetime.now()
print(atual)

mostrardata = datetime(2023,9,23)
print(type(mostrardata))
print(atual.strftime("%d/%m/%y, %H:%M"))
'''

DataNasc = input("Digite sua data de nascimento dd/mm/yyyy: ")
#print(type(DataNasc))
DataNasc = datetime.strptime(DataNasc, "%d/%m/%Y")
print(DataNasc.strftime("%d/%m/%Y"))
#print(type(DataNasc))


hoje = datetime.today()
data = hoje - DataNasc
print(data)
data = hoje.year - DataNasc.year
print(data)
data = hoje.month - DataNasc.month
print(data)


