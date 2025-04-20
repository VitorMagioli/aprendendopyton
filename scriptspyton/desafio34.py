sal = float(input('Salário: R$'))

if sal > 1250:
    aum = ((sal*10)/100) + sal
    print('O novo salário é de: R$ {}'.format(aum))
else:
    aum = ((sal*15)/100) + sal
    print('O novo salário é de: R$ {}'.format(aum))