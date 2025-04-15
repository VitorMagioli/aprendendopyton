n = 0
s = 0
c = 0

for c in range(1, 7):
    n = int(input('Digite um número:'))

    if n % 2 == 0:
        s += n

print('A soma dos valores pares é: {}'.format(s))