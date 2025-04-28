import webbrowser

try:
    url = 'https://www.pudim.com.br/'
    webbrowser.open(url)
    print('Consegui acessar o site pudim com sucesso.!')
except:
    print('\33[0;31m O site pudim não está acessível no momento. \33[m')

    