def soma(a,b):
    s = a+b
    print(s)


def sub(a, b):
    s = a - b
    print(s)


def mult(a, b):
    s = a * b
    print(s)

def div(a, b):
    s = a / b
    print(s)

def cab():
    print('==='*10)
    print('CALCULADORA')
    print('==='*10)

opcao = 0
while True:
    print('MENU: ')
    print('[1] SOMA: ' \
    '                 [2] SUBTRAÇÃO' \
    '                 [3] MULTIPLICAÇÃO' \
    '                 [4] DIVISÃO')
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        a = int(input('1º número: '))
        b = int(input('2º número: '))
        soma(a,b)
        break
    if opcao == 2:
        a = int(input('1º número: '))
        b = int(input('2º número: '))
        sub(a,b)
        break
    if opcao == 3:
        a = int(input('1º número: '))
        b = int(input('2º número: '))
        mult(a,b)
        break
    if opcao == 4:
        a = int(input('1º número: '))
        b = int(input('2º número: '))
        soma(a,b)
        break
    if opcao == 5:
        a = int(input('1º número: '))
        b = int(input('2º número: '))
        soma(a,b)
        break
    if opcao > 5 or opcao < 0:
        print('[OPÇÃO INVÁLIDA] Escolha uma das opções abaixo.')
