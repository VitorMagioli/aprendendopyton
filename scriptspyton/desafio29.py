print('Sistema do Detran')

vel = int(input('Velocidade do Carro no Radar: '))

if vel > 80:
    print('MULTADO! Você ultrapassou o limite de velocidade!')
    m = (vel - 80) * 7
    print('O valor da multa ficou em R$ {:.2f} reais.'.format(m))
else:
    print('Dentro do limite. Dirija com responsabilidade.')