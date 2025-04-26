def ficha(n='<desconhecido>', g=0):
    print(f'O jogador {n} fez {g} gols no campeonato.')

#Programa Principal
nome = str(input('Nome do Jogador: '))
gol = str(input('Gols no Campeonato: '))

if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0

if nome.strip() == '':
    ficha(g=gol)
else:
    ficha(nome, gol)
