from datetime import datetime

anoatual = datetime.now().year

ctps = dict()
print('=== CADASTRO CARTEIRA DE TRABALHO ===')
ctps['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
ctps['idade'] = anoatual - nasc
print('Legenda n° da CTPS: \n[0 - Não Possui]')
ctps['ctps'] = int(input('N° CTPS:  '))

if ctps['ctps'] == 0:
    print('==='*20)
    print('  SUAS INFORMAÇÕES:  ')
    for k, v in ctps.items():
        print(f'{k}: {v}.')
else:
    ctps['contratação'] = int(input('Ano de Contratação: '))
    ctps['salário'] = float(input('Salário: R$ '))
    ctps['aposentadoria'] = ctps['contratação'] + 35
    print('==='*20)
    print('  SUAS INFORMAÇÕES:  ')
    for k, v in ctps.items():
        print(f'{k}: {v}.')
