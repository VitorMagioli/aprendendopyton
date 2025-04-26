from time import sleep

def contador (inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    if inicio < fim:
        c = inicio
        while c <= fim:
            print(f'{c} ', end='', flush=True)
            sleep(0.5)
            c+=passo
        print('FIM!')

    else:
        c = inicio
        while c >= fim:
            print(f'{c} ', end='', flush=True)
            sleep(0.5)
            c-=passo
        print('FIM!')

    #for c in range(inicio, fim+1, passo):
     #   sleep(1)
      #  print(inicio)
       # inicio += passo
        #c+=1



def lin():
    print('==='*30)

lin()
contador(1, 10, 1)
lin()
contador(10, 0, 2)
lin()
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

contador(i, f, p)
