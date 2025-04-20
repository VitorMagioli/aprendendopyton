import datetime
print('-=-'*20)
print('SISTEMA DE ALISTAMENTO')
print('-=-'*20)

nasc = int(input('Informe o ano de nascimento: '))

#importando o ano atual da biblioteca
hoje = datetime.date.today().year

id = hoje - nasc

if id > 18:
    print('Já passou o tempo de alistamento!')
    print('Passou {} anos do prazo para alistamento. Se você não se apresentou procure a Junta de Serviço Militar.'.format(id-18))
elif id > 17:
    print('Está na hora de se alitar! Procure a Junta de Serviço Militar.')
else:
    print('Ainda não chegou o momento de se alistar.')
    print('Faltam {} anos para você se alistar.'.format(18 - id))
