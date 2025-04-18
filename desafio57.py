
sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MmFf':
    print('[ENTRADA INVÁLIDA] Digite novamente!')
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    print('Sexo "{}" registrado com sucesso.'.format(sexo))

