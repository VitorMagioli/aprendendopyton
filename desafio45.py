from random import randint
from time import sleep

item = ('Pedra' , 'Tesoura', 'Papel') #para aparecer na tela a escolha do computador
computador = randint(0, 2) #três possibilidades

print('-=-'*20)
print('      !!!! JOKENPO !!!!     ')
print('-=-'*20)

sleep(1)

print('Escolha entre PEDRA, PAPEL e TESOURA e tente ganhar de mim!')

sleep(1)

print('''
[0] PEDRA\n
[1] TESOURA\n
[2] PAPEL \n
''')

escolha = int(input('Selecione para Jogar: '))

print ('PROCESSANDO...')
sleep(2)

if escolha == computador:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    sleep(1)
    print('\nEMPATE!!!\n')
    print('O computador escolheu {}.\n'.format(item[computador]))

elif escolha == 0 and computador == 1:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    sleep(1)
    print('\n[PEDRA] Parabéns! PEDRA vence TESOURA. Você venceu!!!\n')
    print('O computador escolheu {}.\n'.format(item[computador]))

elif computador == 0 and escolha == 1:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    sleep(1)
    print('\n[PEDRA] Você perdeu! PEDRA vence TESOURA. Computador venceu!!!\n')
    print('O computador escolheu {}.\n'.format(item[computador]))

elif escolha == 1 and computador == 2:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    sleep(1)
    print('\n[TESOURA] Parabéns! TESOURA vence PAPEL. Você venceu!!!\n')
    print('O computador escolheu {}.\n'.format(item[computador]))

elif computador == 1 and escolha == 2:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    sleep(1)
    print('\n[TESOURA] Você perdeu! TESOURA vence PAPEL. Computador venceu!!!\n')
    print('O computador escolheu {}.\n'.format(item[computador]))
    
elif escolha == 0 and computador == 2:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    sleep(1)
    print('\n[PAPEL] Parabéns! PAPEL vence PEDRA. Você venceu!!!\n')
    print('O computador escolheu {}.\n'.format(item[computador]))

elif computador == 0 and escolha == 2:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    sleep(1)
    print('\n[PAPEL] Você perdeu! PAPEL vence PEDRA. Computador venceu!!!\n')
    print('O computador escolheu {}.\n'.format(item[computador]))

else:
    print('[OPÇÃO INVÁLIDA!] Escolha uma das opções acima.')

print('Obrigado por Jogar!')