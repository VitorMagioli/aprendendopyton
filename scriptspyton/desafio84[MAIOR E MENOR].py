dados = list()
pessoas = list()

menor = maior = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))

    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]

        if dados[1] < menor:
            menor = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
    
print(f'Os dados cadastrados foram: {pessoas}')
print(f'Você cadastrou {len(pessoas)} pessoas, ao todo.')
print(f'O maior peso foi de {maior}', end='')
for p in pessoas:
    if p[1] == maior:
        print(f' [{p[0]}]', end='')
print(f'\nO menor peso foi de {menor}', end='')
for p in pessoas:
    if p[1] == menor:
        print(f' [{p[0]}]', end='')
