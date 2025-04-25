from random import randint
from time import sleep
from operator import itemgetter

dado = dict()
ranking = list()
jogadores = 4

#cada jogador recebe um valor aleatório
for k in range(1, jogadores+1):
    dado[f'jogador {k}'] = randint(1,6)

print('Valores sorteados:')

for k, v in dado.items():
    print(f'{k} tirou o valor {v}')
    sleep(1)

print('==='*30)
print('Ranking dos jogadores:')

ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]} pontos.')
    sleep(1)
