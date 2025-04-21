palavras = ('aprender', 'azul', 'luz', 'janela', 'italia', 'grama', 'preto', 'cortina',
             'frio', 'calor', 'mato', 'verde')

for p in palavras:
    print(f'\nNa palavra {p} temos ', end='')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')
            

