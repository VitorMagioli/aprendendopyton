from random import randint
from time import sleep
computador = randint(1, 3) #três possibilidades
print('-=-'*20)
print('      !!!! JOKENPO !!!!     ')
print('-=-'*20)
print('Escolha entre PEDRA, PAPEL e TESOURA e tente ganhar de mim!')

print('''
[1] PEDRA
[2] PAPEL
[3] TESOURA ''')

escolha = int(input('Selecione para Jogar: '))

print ('PROCESSANDO...')
sleep(2)

if escolha == computador:
    print('JO - KEN - PO.....')
    sleep(1)
    print('EMPATE!!!\n')

elif escolha == 1 and computador == 2:
    print('JO - KEN - PO.....\n')
    sleep(1)
    print('[PEDRA] Parabéns! PEDRA vence TESOURA. Você venceu!!!\n')

elif computador == 1 and escolha == 2:
    print('JO - KEN - PO.....\n')
    sleep(1)
    print('[PEDRA] Você perdeu! PEDRA vence TESOURA. Computador venceu!!!\n')

elif escolha == 2 and computador == 3:
    print('JO - KEN - PO.....\n')
    sleep(1)
    print('[TESOURA] Parabéns! TESOURA vence PAPEL. Você venceu!!!\n')

elif computador == 2 and escolha == 3:
    print('JO - KEN - PO.....\n')
    sleep(1)
    print('[TESOURA] Você perdeu! TESOURA vence PAPEL. Computador venceu!!!\n')

elif escolha == 1 and computador == 3:
    print('JO - KEN - PO.....\n')
    sleep(1)
    print('[PAPEL] Parabéns! PAPEL vence PEDRA. Você venceu!!!\n')

elif computador == 1 and escolha == 3:
    print('JO - KEN - PO.....\n')
    sleep(1)
    print('[PAPEL] Você perdeu! PAPEL vence PEDRA. Computador venceu!!!\n')

print('Obrigado por Jogar!')