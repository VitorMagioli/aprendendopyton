print('-=-'*10)
print('           CADASTRO')
print('-=-'*10)
opcao = 'S'
i = h = m = 0
while opcao not in 'N':
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]

    if idade >= 18:
        i+=1
    if sexo == 'M':
        h+=1
    elif sexo == 'F':
        if idade < 20:
            m += 1
    
    opcao = str(input('Deseja continuar cadastrando? [S/N]: ')).upper().strip()[0]
    print('---'*10)
    
print(f'{i} pessoas tem mais de 18 anos.')
print(f'{h} homens foram cadastrados.')
print(f'{m} mulheres tem menos de 20 anos.')

print('-=-'*10)
print('FIM DO PROGRAMA')
print('-=-'*10)
