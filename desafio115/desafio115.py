import funcoes
opcao = 0
while True:
        funcoes.cab('Menu Principal')
        print('''
[1] CADASTRAR UMA PESSOA
[2] VER LISTA DE PESSOAS CADASTRADAS
[3] SAIR DO PROGRAMA      ''')
        opcao = int(input('Sua opção: '))
        try:
            if opcao == 1:
                print('cadastro')
            if opcao == 2:
                print('lista')
            if opcao == 3:
                break
        except:
            print('[ERRO] Digite uma opção válida')
