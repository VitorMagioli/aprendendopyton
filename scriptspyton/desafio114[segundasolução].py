import urllib
import urllib.error
import urllib.request

try:
    url = urllib.request.urlopen('http://www.pudim.com.br/')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso.')
    print(url.read())
