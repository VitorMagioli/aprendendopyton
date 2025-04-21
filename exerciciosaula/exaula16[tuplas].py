lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'

print(lanche)

print(len(lanche))

for comida in lanche:
    print(f'Eu vou comer {comida}')

#pode ser usado sem o 'pos' e o 'enumerate'
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}\n')

for c in range(0, len(lanche)):
    print(f'\nEu vou comer {lanche[c]} na posição {c}')

#comando sorted para ordenar (foi ordenado em ordem alfabética)
print(sorted(lanche))

