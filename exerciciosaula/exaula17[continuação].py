dados = []
informacoes = []
pessoas = []

dados.append('Pedro')
dados.append(25)
dados.append('Maria')
dados.append(19)
dados.append('João')
dados.append(32)

print(dados) 

informacoes.append('Rua pedro')
informacoes.append('Rua maria')
informacoes.append('Rua João')
print(informacoes)

pessoas.append(dados[:]) #faz uma cópia da lista dados para a lista pessoas e fica como elemento 0
pessoas.append(informacoes[:]) #faz uma cópia da lista informações para a lista pessoas e fica como elemento 1
print(pessoas)

print(pessoas[0][2])
print(pessoas[0][4])

print(pessoas[1][0])
print(pessoas[1][2])#mostra o elemento dentro do elemento

print(pessoas[1])#mostra o primeiro elemento da lista dentro da lista(lista inteira)

for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade.')
    