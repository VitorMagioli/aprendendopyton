from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

menu = 0

while menu != 5:
    sleep(1)
    print ('''
    [1] SOMAR
    [2] MULTIPLICAR 
    [3] MAIOR VALOR
    [4] NOVOS NÚMEROS
    [5] SAIR''')

    menu = int(input('Escolha uma opção: '))

    if menu == 1:
        s = n1 + n2
        sleep(1)
        print('A soma entre {} mais {} é igual a {}.'.format(n1, n2, s))
    
    elif menu == 2:
        s = n1 * n2
        sleep(1)
        print ('A multiplicação entre {} e {} é igual a {}.'.format(n1, n2, s))
    
    elif menu == 3:
        if n1 > n2:
            sleep(1)
            print ('{} é maior que {}'.format(n1, n2))
        else:
            sleep(1)
            print('{} é maior que {}'.format(n2, n1))
    
    elif menu == 4:
        n1 = int(input('Digite o 1º novo valor: '))
        n2 = int(input('Digite o 2º novo valor: '))
        sleep(1)

    elif menu == 5:
        print('Finalizando....')
        sleep(1)
    else:
        sleep(1)
        print('[OPÇÃO INVÁLIDA] Escolha uma das opções acima!')

    print('=-='*10)
    
print('-- FIM DO PROGRAMA --')
