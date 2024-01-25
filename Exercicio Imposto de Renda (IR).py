print("Olá seja bem vindo")
nome = input("Digite seu usuário : ")

Salario1 = float(input("Informe seu salário : "))

#Cálculo INSS

if Salario1 > 1100.01:
    Inssb= 0.09
elif Salario1 > 6433.57:
    inss = 900.70
elif Salario1 > 2203.49:
     Inssb = 0.12
elif Salario1 > 3205.22:
     Inssb = 0.14
else:
     Inssb = 0.075


INSS = Salario1 * Inssb

base = Salario1 - INSS

#Cálculo IR

if base > 4664.68:
    IRP = 0.275
    deducao = 869.36
elif base > 3751.06:
     IRP= 0.225
     deducao = 363.13
elif base > 2826.66:
     IRP= 0.15
     deducao= 354.80
elif base > 1903.99:
    IRP = 0.075
    deducao= 142,80
else:
    IRP = 0
    deducao = 0


IR = (base*IRP) - deducao

SalarioL= base - IR

print('Salário Bruto: {:.2f}\n Salário Base: {:.2f}\nINSS: {:.2f}\n%IR: {:.2f}%\nValor IR: {:.2f}\nSalário Líquido :{:.2f}'.format(Salario1, base, INSS, IRP*100, IR, SalarioL))



    

