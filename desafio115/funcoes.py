def cab(msg):
    tam = len(msg)
    print('---'*tam)
    print(f'{msg:^{tam*3}}')
    print('---'*tam)

def cadastroPessoa():
    cab('Novo Cadastro')
    pessoa = dict()
    try:
        pessoa['nome'] = str(input('Nome: '))
        pessoa['idade'] = int(input('Idade: '))
    except:
        print('Dados inválidos. Verifique os dados inseridos e tente novamente.')
    else:
        print(f'Novo Registro de {pessoa["nome"]} adicionado.')

def listaPessoa():
    cab('Pessoas Cadastradas')
    for pos in range(0, cadastroPessoa.len(pessoa)):
        if pessoa['nome']:
            print(f'{pessoa['nome'][pos]:.<30}', end='')
        else:
            print(f'{pessoa['nome'][pos]:<30.2f}')
