def cab():
    print('=='*13)
    print('CÁLCULO DA ÁREA DE TERRENO')
    print('=='*13)

def calculo(l, c):
    calc = l * c
    print(f'A área do terreno {l}m por {c}m tem {calc}m².')

cab()

l = float(input('LARGURA (m): '))
c = float(input('Comprimento (m): '))

calculo(l, c)
