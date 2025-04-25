def soma(a,b):
    s = a+b
    print(f'A soma entre {a} e {b} é igual a {s}')


def sub(a, b):
    s = a - b
    print(f'A subtração entre {a} e {b} é igual a {s}')


def mult(a, b):
    s = a * b
    print(f'A multiplicação entre {a} e {b} é igual a {s}')

def div(a, b):
    s = a / b
    print(f'A divisão entre {a} e {b} é igual a {s}')

def cab():
    print('=='*10)
    print('     CALCULADORA')
    print('=='*10)


opcao = 0
while True:
    cab()
    print('     MENU: ')
    print('''    [1] SOMA 
    [2] SUBTRAÇÃO
    [3] MULTIPLICAÇÃO
    [4] DIVISÃO''')
    
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
        div(a,b)
        break
    if opcao > 4 or opcao < 0:
        print('[OPÇÃO INVÁLIDA] Escolha uma das opções abaixo.')
