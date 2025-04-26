from time import sleep

def contador (inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    for c in range(inicio, fim+1, passo):
        sleep(1)
        print(inicio)
        inicio += passo
        c+=1
    print('FIM!')


def lin():
    print('==='*30)

lin()
contador(1, 10, 1)
lin()
contador(10, 0, -2)
lin()
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

contador(i, f, p)
