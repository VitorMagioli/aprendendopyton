import funcoes
opcao = 0
while True:
        funcoes.cab('Menu Principal')
        print('''
[1] CADASTRAR UMA PESSOA
[2] VER LISTA DE PESSOAS CADASTRADAS
[3] SAIR DO PROGRAMA      ''')
        
        opcao = int(input('Sua opção: '))
        if opcao == 1:
            print('Chamando função cadastroPessoa...')
            funcoes.cadastroPessoa()
        if opcao == 2:
            print('lista')
        if opcao == 3:
            break
