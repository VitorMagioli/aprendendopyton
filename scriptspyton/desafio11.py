print('Calcular Quantidade de Tinta para Pintar uma Parede')

lar = int(input('Largura da parede: '))
alt = int(input('Altura da parede: '))

area = lar * alt

print('Você precisa de {} litros de tinta para pintar a parede.'.format(area/2))