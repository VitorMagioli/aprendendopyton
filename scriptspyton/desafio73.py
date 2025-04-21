brasileirao = ('Palmeiras', 'Flamengo', 'Fluminense', 'Bragantino', 'Ceará', 'Corinthians', 'Cruzeiro', 'Vasco', 'Juventude', 'São Paulo', 'Mirassol', 'Internacional', 'Fortaleza', 'Botafogo', 'Vitória', 'Atlético-MG', 'Santos', 'Grêmio', 'Bahia', 'Sport')

print(f'Os cinco primeiros colocados do brasileirão são: {brasileirao[:5]}\n')

print(f'Os quatro últimos colocados do brasileirão são: {brasileirao[16:]}\n')

print(sorted(brasileirao))
print('\n')
print(f'O {brasileirao[8]} está na {(brasileirao.index("Juventude")+1)}ª posição.\n')

print('==='* 20)
print('Classificação do Brasileirão:')

for c in range(0, len(brasileirao)):
    print(f'{(c+1)}ª posição: {brasileirao[c]}')