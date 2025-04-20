r = 'S'
q = s = maior = menor = 0
while r in 'Ss':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    s += n
    q += 1
    if q == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

m = s / q
print('Você digitou {} números.'.format(q))
print('A média dos números digitados é: {:.2f}'.format(m))
print('O maior número é {} e o menor número é {}'.format(maior, menor))
print('FIM')
