n = c = s = 0
n = int(input('Digite um número: '))
while n != 999:
    c += 1
    s += n
    n = int(input('Digite um número: '))
    
print('Você digitou {} números.'.format(c))
print('A soma dos números digitados é: {}'.format(s))
print('FIM')