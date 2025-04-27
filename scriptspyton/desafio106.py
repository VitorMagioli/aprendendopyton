c = ('\033[m',          #0 - sem cores
     '\033[0;30;41m',    #1 - vermelho
     '\033[0;30;42m',    #2 - verde
     '\033[0;30;43m',    #3 - amarelo
     '\033[0;30;44m',    #4 - azul
     '\033[0;30;45m',    #5 - roxo
     '\033[7;30m'       #6 - branco
     );

def cab(msg, cor=0):
    tam = len(msg)
    print(c[cor], end='')
    print('~'*tam)
    print(msg)
    print('~'*tam)
    print(c[0], end='')

def ajuda(com):
    cab(f'Acessando a ajuda do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')

#Programa Principal
comando = ''
while True:
    cab('Sistema de Ajuda PyHelp', 2)

    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

cab('ATÉ LOGO!', 1)
