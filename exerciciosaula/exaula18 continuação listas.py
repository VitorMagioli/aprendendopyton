pessoas = list()

dados = list()

for c in range(0,3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))

    pessoas.append(dados[:])
    dados.clear()#apaga a lista dados
print(pessoas)
totmai = totmen = 0
#mostrar lista das pessoas com mais de 21 anos
for p in pessoas:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai +=1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen +=1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')
