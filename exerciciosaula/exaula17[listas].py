print('==='*30)
print('PRIMEIRA LISTA')
lista = [1, 5, 4, 6, 8, 9, 3]
print (f'Lista OriginaL: {lista}')

#insere valor na posição selecionada
lista[3] = 2
print(f'Lista alterada com 2 no lugar do 6: {lista}')

#insere valor no FINAL da lista
lista.append(6)

#insere valor na posição selecionada, primeiro elemento POSIÇÃO, segundo elemento VALOR INSERIDO
lista.insert(4, 7)
print(f'Lista com 6 inserido por comando APPEND e 7 inserido por comando INSERT: {lista}')

#lista ordenada CRESCENTE
lista.sort()
print(f'Lista ordenada crescente: {lista}')

#lista ordenada DECRESCENTE
lista.sort(reverse=True)
print(f'Lista ordenada decrescente: {lista}')
print(f'Essa lista tem {len(lista)} elementos')

#remove valor do final
lista.pop()
print(f'Lista com último elemento removido: {lista}')

#deleta valor da posição selecionada
lista.pop(5)
print(f'Lista com elemento da posição 5 removido: {lista}')

#remove o primeiro valor que aparece na lista
#se houverem mais de um valor 9 na lista só a primeira ocorrência será removida.
lista.remove(9)
print(f'Número 9 removido da lista: {lista}')


#TRATAMENTO DE EXCEÇÃO
#condição para remover um valor da lista caso possua
if 1 in lista:
    lista.remove(4)
else:
    print('Não achei o número 4.')

print('==='*30)
print('PRÓXIMA LISTA')

valores = []
#valores = list() // PODE SER DECLARADO ASSIM PARA CRIAR UMA LISTA VAZIA

valores.append(3)
valores.append(8)
valores.append(1)

for c, v in enumerate(valores):
    print(f'Encontrei o valor {v} na posição {c}')

#ESSE COMANDO [:] CRIA UMA CÓPIA DA LISTA PARA OUTRA LISTA
b = valores [:]
b[1] = 0
print (b)


#CRIANDO UMA LISTA PARA RECEBER VALORES DO USUÁRIO
print('==='*30)
print('RECEBENDO VALORES DO USUÁRIO')
itens = list()
for c in range(5):
    itens.append(int(input('Digite o valor que deseja armazenar: ')))

print(f'\nOs valores armazenados foram{itens}')
