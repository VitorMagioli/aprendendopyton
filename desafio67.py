print('-=-'*20)
print('PROGRAMA TABUADA')
print('-=-'*20)

n = 0

while n >= 0:
    c = m = 0
    n = int(input('''Quer ver a tabuada de qual valor? 
[PARA SAIR] DIGITE UM VALOR NEGATIVO: '''))

    if n < 0:
        break

    while c <= 10:
        m = n * c
        print(f'{n} x {c} = {m}')
        c+=1

print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')
