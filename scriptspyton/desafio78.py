valores = list()
for c in range(5):
    valores.append(int(input(f'Digite o valor da posição {c}: ')))

print('==='*20)
print(f'Você digitou os valores {valores}')

print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
for v in range(0, len(valores)):
    if valores[v] == max(valores):
        print(f'{v}...', end='')

print()
print(f'O menor valor digitado foi {min(valores)} nas posições ', end='')
for v in range(0, len(valores)):
    if valores[v] == min(valores):
        print(f'{v}... ', end='')
