numeros = list()
pares = list()
impares = list()
n = 0
for c in range(0, 7):
    n = int(input(f'Digite o {c+1}º valor: '))
    
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    
pares.sort()
impares.sort()
numeros.append(pares[:])
numeros.append(impares[:])
pares.clear()
impares.clear()
    
print(numeros)

print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores ímpares digitados foram: {numeros[1]}')
