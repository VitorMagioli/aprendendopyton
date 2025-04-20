from datetime import date
print('-=-'*20)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('-=-'*20)

nasc = int(input('Ano de nascimento: '))
hoje = date.today().year

ano = hoje - nasc

if ano < 9:
    print('MIRIM')
elif ano < 14:
    print('INFANTIL')
elif ano < 18:
    print('JÚNIOR')
elif ano < 20:
    print('SÊNIOR')
else:
    print('MASTER')