print('Cálculo Valor de Passagem')

dis = float(input('Digite a distância da viagem(em km): '))

if dis <= 200:
    preco = dis * 0.5
    print('A viagem custará R$ {:.2f}'.format(preco))
else:
    preco = dis * 0.45
    print('A viagem custará R$ {:.2f}'.format(preco))