brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil)

print(brasil[1]['sigla'])
print(brasil[0]['uf'])

print('==='*30)

estado = dict()
brasil = list()

for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))

    brasil.append(estado.copy()) #função interna para copiar as informações do dicionário para lista.

print(brasil)

for e in brasil:
   print(e)

for e in brasil:
    for k, v in e.items():
        print(f'{k} - {v}')
        print()

for e in brasil:
    for v in e.values():
        print(v, end=' ')
        print()
