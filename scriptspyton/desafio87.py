matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

for c in range (0, 3):
    for i in range(0, 3):
        matriz[c][i] = int(input(f'{[c, i]}: '))


for c in range (0, 3):
    for i in range(0, 3):
        print(f'[{matriz[c][i]:^5}]', end='')
    print()

print('==='*20)
pares = 0

for c in range (0, 3):
    for i in range(0, 3):
        if matriz[c][i] % 2 == 0:
            pares += matriz[c][i]
        
tcoluna = 0
for c in range (0, 3):
    if matriz[c][2]:
        tcoluna += matriz[c][2]

maior = 0
for c in range (0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]

print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é: {tcoluna}.')
print(f'O maior valor da segunda linha é: {maior}.')
