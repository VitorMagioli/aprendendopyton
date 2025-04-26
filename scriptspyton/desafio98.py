from time import sleep

def contador (inicio=0, fim=0, passo=0): #PARÂMETROS OPCIONAIS
    #INTERACTIVE HELP
    """
    - faz uma contagem e mostra na tela.
    :param inicio: inicio da contagem
    :param fim: fim da contagem
    :param passo: passo da contagem
    :return: sem retorno
    :Função criada por Vitor Magioli
    """
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    if inicio < fim:
        c = inicio #VARIÁVEL DE ESCOPO LOCAL
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

help(contador)
#PROGRAMA PRINCIPAL
lin()
contador(1, 10, 1)
lin()
contador(10, 0, 2)
lin()
print('Agora é sua vez de personalizar a contagem!')
#VARIÁVEIS DE ESCOPO GLOBAL
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

contador(i, f, p)
