r = 'S'
q = s = 0
while r in 'Ss':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    s += n
    q += 1

m = s / q
print('Você digitou {} números.'.format(q))
print('A média dos números digitados é: {}'.format(m))
print('FIM')
