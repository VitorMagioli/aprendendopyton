print('-=-'*20)
print('                     CAIXA DA LOJA')
print('-=-'*20)

preco = float(input('Valor do produto: '))
print ('''
[1] PAGAMENTO A VISTA (dinheiro ou PIX)
[2] PAGAMENTO A VISTA (CARTÃO)
[3] PAGAMENTO em até 2x no Cartão
[4] PAGAMENTO em 3x ou mais no Cartão
''')
pagamento = int(input('Selecione a forma de Pagamento: '))

valorfinal = 0

if pagamento == 1:
    valorfinal = preco - ((preco * 10) / 100)        
    print ('Valor Final: R$ {}'.format(valorfinal))
elif pagamento == 2:
    valorfinal = preco - ((preco * 5) / 100)
    print ('Valor Final: R$ {}'.format(valorfinal))
elif pagamento == 3:
    print ('Valor Final: R$ {}'.format(preco))
elif pagamento == 4:
    valorfinal = preco + ((preco * 20) / 100)
    print ('Valor Final: R$ {}'.format(valorfinal))

print('Obrigado pela Preferência. Volte Sempre!')