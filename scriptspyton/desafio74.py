from random import randint

#c1 = randint(0, 5)
#c2 = randint(0, 5)
#c3 = randint(0 ,5)
#c4 = randint(0, 5)
#c5 = randint(0, 5)

#outra forma de fazer números aleatórios numa tupla
numale = (randint(0,5), randint(0,5), randint(0,5), randint(0,5), randint(0,5))

print(f'Os números sorteados foram: ', end='')

for n in numale:
    print(f'{n}, ', end='')

print(f'\nO maior valor sorteado foi {max(numale)}')
print(f'\nO menor valor sorteado foi {min(numale)}')