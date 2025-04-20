n = int(input('Digite o número da tabuada que você quer saber: '))

for c in range (1 , 11):
    print('{} x {} = {}'.format(n, c, n*c))
