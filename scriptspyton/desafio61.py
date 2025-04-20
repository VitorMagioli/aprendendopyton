a1 = int(input('Digite o primeiro valor da P.A: '))
r = int(input('Digite a Razão da P.A: '))

c = 1
termo = a1

#for c in range(1, 11):
#    a = a1 + (c-1) * r
while c <= 10:
    print('{} -> '.format(termo), end='')
    termo += r
    c += 1
print('FIM')