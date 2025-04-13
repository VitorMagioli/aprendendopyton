from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador "pensar"
print('      Jogo de Adivinhação     ')
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!')
print('-=-'*20)

num = int(input('Digite o número que você acha que é: ')) #jogador tenta adivinhar

print ('PROCESSANDO...')
sleep(3)

if num == computador:
    print('Eu pensei em... {}'.format(computador))
    sleep(1)
    print('Você acertou! PARABÉNS!!!!!')
else:
    print('Eu pensei em... {}'.format(computador))
    sleep(1)
    print('Você errou! Tente novamente')