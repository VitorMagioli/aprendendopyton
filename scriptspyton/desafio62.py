a1 = int(input('Digite o primeiro valor da P.A: '))
r = int(input('Digite a Razão da P.A: '))

c = 1
termo = a1
opcao = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print('{} -> '.format(termo), end='')
        termo += r
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos mais você quer ver? '))
print('FIM')