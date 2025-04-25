aluno = dict()

aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input(f'Média do {aluno["nome"]}: '))
if aluno['media'] < 7:
    aluno['situação'] = 'REPROVADO'
else:
    aluno['situação'] = 'APROVADO'

for k, v in aluno.items():
    print(f'{k}: {v}.')
