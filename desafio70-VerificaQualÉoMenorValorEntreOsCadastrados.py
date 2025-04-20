t = m = menor = contador = 0
barato = ' '
while True:
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    contador += 1

    t += preco

    if preco > 1000:
        m += 1

    #VERIFICA QUAL PRODUTO É O MAIS BARATO
    #QUAL É O MENOR ENTRE OS CADASTRADOS
    if contador == 1 or preco < menor:
        menor = preco
        barato = nome
        
        #outra opção de achar o menor produto em complemento ao IF acima
        # else:
        # if preco < menor:
        # menor = preco
        # barato = nome
    
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]

    if opcao == 'N':
        break

print(f'Total da compra: R$ {t}')
print(f'{m} produto(s) acima de R$ 1000.')
print(f'O produto mais barato foi o(a) {barato} que custa {menor:.2f}')
