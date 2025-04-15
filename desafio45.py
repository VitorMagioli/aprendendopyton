from random import randint
from time import sleep
item = ('Pedra' , 'Tesoura', 'Papel')
computador = randint(0, 2) #três possibilidades
print('-=-'*20)
print('      !!!! JOKENPO !!!!     ')
print('-=-'*20)
print('Escolha entre PEDRA, PAPEL e TESOURA e tente ganhar de mim!')

print('''
[0] PEDRA
[1] TESOURA
[2] PAPEL ''')

escolha = int(input('Selecione para Jogar: '))

print ('PROCESSANDO...')
sleep(2)

if escolha == computador:
    print('JO - KEN - PO.....')
    sleep(1)
    print('EMPATE!!!\n')
    print('O computador escolheu {}.'.format(item[computador]))

elif escolha == 0 and computador == 1:
    print('JO - KEN - PO.....\n')
    sleep(1)
    print('[PEDRA] Parabéns! PEDRA vence TESOURA. Você venceu!!!\n')
    print('O computador escolheu {}.'.format(item[computador]))

elif computador == 0 and escolha == 1:
    print('JO - KEN - PO.....\n')
    sleep(1)
    print('[PEDRA] Você perdeu! PEDRA vence TESOURA. Computador venceu!!!\n')
    print('O computador escolheu {}.'.format(item[computador]))

elif escolha == 1 and computador == 2:
    print('JO - KEN - PO.....\n')
    sleep(1)
    print('[TESOURA] Parabéns! TESOURA vence PAPEL. Você venceu!!!\n')
    print('O computador escolheu {}.'.format(item[computador]))

elif computador == 1 and escolha == 2:
    print('JO - KEN - PO.....\n')
    sleep(1)
    print('[TESOURA] Você perdeu! TESOURA vence PAPEL. Computador venceu!!!\n')
    print('O computador escolheu {}.'.format(item[computador]))
    
elif escolha == 0 and computador == 2:
    print('JO - KEN - PO.....\n')
    sleep(1)
    print('[PAPEL] Parabéns! PAPEL vence PEDRA. Você venceu!!!\n')
    print('O computador escolheu {}.'.format(item[computador]))

elif computador == 0 and escolha == 2:
    print('JO - KEN - PO.....\n')
    sleep(1)
    print('[PAPEL] Você perdeu! PAPEL vence PEDRA. Computador venceu!!!\n')
    print('O computador escolheu {}.'.format(item[computador]))

else:
    print('[OPÇÃO INVÁLIDA!] Escolha uma das opções acima.')

print('Obrigado por Jogar!')