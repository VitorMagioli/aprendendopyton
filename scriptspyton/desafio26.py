frase = str(input('Digite a frase: ')).lower()

print('A letra "A" aparece {} na frase.'.format(frase.count('a')))

print('Aparece na posição {} pela primeira vez.'.format(frase.find('a')+1))

print('Aparece na posição {} pela última vez.'.format(frase.rfind('a')+1))