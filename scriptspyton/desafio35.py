print('Formando um triângulo')

r1 = int(input('Digite o valor da primeira reta(em cm): '))
r2 = int(input('Digite o valor da segunda reta(em cm): '))
r3 = int(input('Digite o valor da terceira reta(em cm:) '))

if r1+r2 > r3 and r2+r3 > r1 and r1+r3 > r2:
    print('É possível formar um triângulo com essas medidas!')
else:
    print('não é possível formar um triângulo com essas medidas.')
    