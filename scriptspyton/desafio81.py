lista = []
opcao = ''
while True:
    lista.append(int(input('Digite um número: ')))
    opcao = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if opcao == 'N':
        break

print(f'Foram digitados {len(lista)} números.\n')

print(lista)
print()
if 5 in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')

lista.sort(reverse=True)
print(f'Lista na ordem decrescente: {lista}')