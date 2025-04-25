jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input('Partidas jogadas: '))
golsfeitos = total = 0
for c in range(1, partidas+1):
    golsfeitos = int(input(f'Gols feitos na partida {c}: '))
    c+=1
    gols.append(golsfeitos)
    total += golsfeitos

jogador['gols'] = gols
jogador['total'] = total
print('==='*30)
print(jogador)
print('==='*30)
for k, v in jogador.items():
    print(f'{k}: {v}')
print('==='*30)

print(f'O {jogador["nome"]} jogou {partidas} partidas.')

for i, v in enumerate(gols):
    print(f'=> Na {i+1}ª partida , fez {v} gol(s). ')

print(f'=> Total de {total} gols.')
