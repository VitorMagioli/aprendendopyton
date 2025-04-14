valCasa = float(input('Valor da Casa:R$ '))
salComprador = float(input('Salário do Comprador:R$ '))
anos = int(input('Quantos anos? '))

meses = anos * 12

prestacao = valCasa / meses

if prestacao > ((salComprador*30)/100):
    print('FINANCIAMENTO NEGADO! O valor do financiamento R$ {:.2f} excede em mais de 30 porcento o salário do comprador.'.format(prestacao))
else:
    print('PARABÉNS! Você conseguiu adquirir seu imóvel. O valor da sua parcela mensal é R$ {:.2f}'.format(prestacao))
