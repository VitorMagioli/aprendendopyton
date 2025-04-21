valores = list()
r = ''
while r != 'N':
    n = (int(input('Digite o valor: ')))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor já cadastrado.')
    r = str(input('Deseja continuar? [S/N]')).upper()

valores.sort()
print(f'Você digitou os valores {valores}')
