#parametro recebendo valores sem saber quantos
#método chamado de DESEMPACOTAMENTO
def contador(*num):
    for valor in num:
        print(f'{valor}, ', end='')
    print('FIM!')
    tam = len(num)
    print(f'Recebi os valores {num} e são {tam}, ao todo.')

contador(2,4,6,8,10)
contador(7,6,3,2,1,5,9,6,5,1,3,0)

print()
print('='*30)

#função recebendo uma lista como parâmetro
#função dobra o valor da lista
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [2,3,6,5,7]
dobra(valores)#executa a função definida acima
print(valores)

print()
print('='*30)

#OUTRO EXEMPLO DE DESEMPACOTAMENTO
def soma(*valores):
    s = 0
    for n in valores:
        s += n
    print(f'A soma dos valores {valores} é igual a {s}.')

soma(4,8,3,5)
soma(5,2,1)
print()
print('='*30)
