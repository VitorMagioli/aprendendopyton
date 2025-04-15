a1 = int(input('Digite o primeiro valor da P.A: '))
r = int(input('Digite a Razão da P.A: '))

c = 0
a = 0

for c in range(1, 11):
    a = a1 + (c-1) * r
    print('Termo {}: {}')