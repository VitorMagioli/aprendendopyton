from random import randint
from time import sleep
computador = randint(0, 10) #faz o computador "pensar"
print('      Jogo de Adivinhação     ')
print('-=-'*20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar!')
print('-=-'*20)

acertou = False
palpite = 0

while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpite += 1
    print ('PROCESSANDO...')
    sleep(1)

    if jogador == computador:
        acertou = True

    elif jogador < computador:
        print('Mais... Tente mais uma vez.')
        print ('PROCESSANDO...')
        sleep(1)
    else:
        print('Menos... Tente mais uma vez.')
        print ('PROCESSANDO...')
        sleep(1)
print('Acertou com {} tentativas. Parabéns!'.format(palpite))
