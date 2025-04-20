from random import randint
from time import sleep

print('-=-'*10)
print('PROGRAMA TABUADA')
print('-=-'*10)
sleep(1)
v = 0

while True:
    s = 0
    computador = randint(0,10)
    n = int(input('Escolha um valor: '))
    
    s = computador + n
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P/I]: ')).upper().strip()[0]
    sleep(1)
    print(f'Você jogou {n} e o computador jogou {computador}. Total de {s}', end='')
    print(', DEU PAR' if s % 2 == 0 else ', DEU ÍMPAR')
    
    if tipo == 'P':
        if s % 2 == 0:
            sleep(1)
            print('-=-'*10)
            print('Você VENCEU!\nVamos jogar novamente...')
            print('-=-'*10)
            v+=1
        else:
            sleep(1)
            print('-=-'*10)
            print('Você PERDEU\nObrigado por jogar!')
            print('-=-'*10)
            break
    elif tipo == 'I':
        if s % 2 == 1:
            sleep(1)
            print('-=-'*10)
            print('Você VENCEU!\nVamos jogar novamente...')
            print('-=-'*10)
            v+=1
        else:
            sleep(1)
            print('-=-'*10)
            print('Você PERDEU\nObrigado por jogar!')
            print('-=-'*10)
            break
sleep(1)
print(f'[GAME OVER] Você venceu {v} vezes.')
