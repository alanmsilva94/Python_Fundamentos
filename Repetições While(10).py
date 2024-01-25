# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.


from random import randint

c = 0

while True:
    opcao = ' '
    while opcao not in 'PI':
        # UPPER para deixar a letra maiúscula, STRIP para cortar os espaços e [0] para selecionar a primeira letra da string
        opcao = str(input('Esolha PAR ou IMPAR [P/I]:')).upper().strip()[0]
    jogador = int(input('Esolha um número: '))
    pc = randint(0, 10)
    total = jogador + pc
    print(f'Você escolheu {jogador} e o pc escolheu {pc} o total foi de {total}')
    print('Deu Par' if total % 2 == 0 else 'Deu Impar' )
    if opcao == 'P':
        if total % 2 == 0:
            print('Você ganhou!')
            c = c + 1
        else:
            print('Você perdeu!')
            break
    elif opcao == 'I':
        if total % 2 == 1:
            print('Você ganhou!')
            c += 1
        else: 
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'Game Over! Você ganhou {c} vezes!')




    