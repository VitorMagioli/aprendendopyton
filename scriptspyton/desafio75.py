n = (int(input('Digite um número para armazenar: ')), int(input('Digite um número para armazenar: ')), int(input('Digite um número para armazenar: ')), int(input('Digite um número para armazenar: ')))

print(f'Você digitou os valores: {n}\n')
#mostrar quantas vezes apareceu o valor 9
print(f'O valor 9 apareceu em {n.count(9)} vezes.')
if 3 in n:
    print(f'O valor 3 apareceu pela primeira vez na {n.index(3)+1}ª posição.')
else: 
    print('O valor 3 não foi digitado em nenhuma posição.')

print('Os valores pares digitados foram ', end='')

for num in n:
    if num % 2 == 0:
        print(num, end=' ')
